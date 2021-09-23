Linux Kernel Development
=================================

.. image:: _static/imgs/LinuxKernelDevelopment_2010_imgs/cover.jpg
   :align: center
   :scale: 60%

Process Management
------------------

The kernel does not an internal representation for threads. Actually it does not find threads to be that different then processes. 

All processes are stored in a doubly-linked list where each element is a descriptor of type ``struct task_struct``. Additionally each processes gets assigned an opaque unique identification called pid [#f1]_, which is used as an indexk

.. image:: _static/imgs/LinuxKernelDevelopment_2010_imgs/struct_task_list.png
   :scale: 80%

Usually when the kernel operates on processes, it accesses directly the ``task_struct`` of the target process. It is quite common to edit the values associated with a certain process, often that is the currently executing process. Henceforth, a mechanism for acquiring it is provided - the ``current()`` macro. Its implementation is architechture specific and depends on other factors discussed later.

In order to access the ``task_struct`` of a process, firstly the ``struct thread_info`` must be acquired and then access the other, which is pointed by one of the members of ``thread info``. It is usually stored at the bottom or the top of the kernel stack, or a pointer to it is stored in a register, depending on the specific arch.

Each process is in exactly one of the following states:

  * ``TASK_RUNNING`` - The task is in the run queue, meaning that it is either runable or actually running
  * ``TASK_INTERRUPTIBLE`` - The task is blocked and resides in a wait queue and awaits for a specific event, which will *interrupt* its sleep. Also, if it receives a signal, it might awake prematurely.
  * ``TASK_UNINTERRUPTIBLE`` - Same as previous but cannot wake up prematurely.
  * ``__TASK_TRACED`` - The task is being traced.
  * ``__TASK_STOPPED`` - The task is not allowed to execute. Usually follows a ``SIGSTOP`` or similar.

The transition is illustrated here:

.. image:: _static/imgs/LinuxKernelDevelopment_2010_imgs/process_state_flow.png
   :scale: 60%

The process state could be modified by the ``set_task_task()`` and ``__set_task_state()`` macros.

The first process (``pid = 1``) is named **init**. It starts executing at the last stage of the boot process. Its ``struct task`` is statically allocated (called ``init_task``).

Creation
^^^^^^^^

The operation of process initialization is twofold - first, ``fork()`` creates a child process with copied parent properties and data, and then ``exec()`` loads a new executable and starts executing it.

.. note::
       Instead of actually copying the parent's address space and other data, a Copy-On-Write methodology is used, meaning that until an actual write operation, the "copied" resources are actually shared between the parent and its child.

The callstack when executing ``fork()`` eventually looks like that:

        1. ``fork ()`` 2. ``clone ()`` 3. ``do_fork ()``
        4. ``copy_process ()`` -- This function performs the majority of the work

           1. It duplicates the descriptors of the parent (``struct task_struct``, ``struct thread_info``)
           2. Updates some of the values of these descriptors to initial or poison values
           3. Sets the process to ``TASK_UNINTERRUPTIBLE``
           4. Allocates a pid
           5. Depending on the passed flag configuration the resources are either shared or cloned.

.. note::
        As we mentioned earlier, threads and processes are not so different in kernelland in terms of representation. This is clearly seen here, ``clone(SIGCHLD, 0);`` is called from "regular" ``fork()``, whilst ``clone(CLONE_VM, CLONE_FS, CLONE_FILES, CLONE_SIGHAND, 0);`` is called when creating a thread.

In the kernel, there exist a notion of solely kernel-executing threads, which *do not* context switch into userland. Furthermore, they do not have their own address space (their ``mm`` pointer equals ``NULL``). All of them are forked off the ``kthreadd``. (The interface is defined in ``<linux/kthread.h>``).

Termination
^^^^^^^^^^^

Process termination is handled mostly by the ``do_exit()`` function (``kernel/exit.c``).

        1. Sets flag in the ``task_struct`` of the process which denotes that the process is exiting.
        2. Removes kernel timers associated with the process.
        3. Releases the address space. If the cound of processes which use it equals 0, it is also destroyed.
        4. Dequeue from IPC semaphores.
        5. Decrements the usage count of objects related  to file descriptors and other file system data.
        6. Stores a copy of the exit code.
        7. Notifies the parent of the process' untimely demise.
        8. Calls ``schedule()``, which performs a context switch. The process never gets scheduled again, and therefor it never returns from the ``schedule()`` call.

A problem arises when the parent exits before the child, the child will forever remain a zobie. The solution is to reparent either to another process from the same thread group, or to the ``init`` process itself.

.. rubric:: Footnotes

.. [#f1] An opaque type is a type whose concrete structure is not exposed, enforcing information hiding.


Process Scheduling
------------------

The fundamental decision which the scheduler has to make is the following: Given a set of processes, which one should execute now?

Multitasking - the art of interleaving execution of multiple tasks, is based on either *preemptive* or *cooperative* multitasking scheme.

Preemptive multitasking
        The scheduler has full control over which process executes and when it executes. It has the power to cease the execution of process A and to resume the execution of process B, and then to repeat this same action with it after some time. This involuntary suspencion is called preemption.
        This mechanism is based on a value (usually referred to as *timeslice* or something along the lines), which represents the amount of time which the process has to execute. The timeslice may be preset or dynamically calculated.

Cooperative multitasking
        Rather than having full control over the current process, the scheduler delegates these power to each and every process. Instead of being forced to "pause" (or rather - directly suspended), the process decides on its own when to *yield*, when to allow other processes to get some CPU time. The negative possibilities are apparent - a process may decide not to yield... ever.

.. note::
        For the couple decades systems utilizing cooperative multitasking are not prevalent. For obvious reasons.

Before Linux 2.6.23, the scheduler had not been transformed since its original implementation. **TODO: Add description of original scheduler**. The transformation resulted in what is nowadays known as the O(1) scheduler. It improves on the limitations of the original scheduler, by introducing a constant-time algorithm for timeslice calculation, as well as adding per-processor run queues.

However, although the O(1) completety outperforms the previous scheduler in regular tasks, when it comes to interactive programs (ones which expect used input, i.e desktop applications), it was kind of bad. Therefoce a new concept turned up and it resulted in the `Completely Fair Scheduler <https://en.wikipedia.org/wiki/Completely_Fair_Scheduler>`_ which is currently being used.

Scheduler Policy
^^^^^^^^^^^^^^^^

These are the rules by which new processes are picked and ran. It has to satisfy two goals:
        1. Low latency
        2. High throughput

Each process could be classfied in one the following two categories:

I/O Bound
        Spend most of their time in submitting and waiting on I/O requests. Therefore, it is running (and runnable) for only short periods of time, because it has to block, while waiting for response. Example for I/O bound process is each and every GUI application ever.

or

CPU Bound
        Spend most of their time executing instructions. Generally executed until preempted (do not block often). An example is the program ssh-keygen.

.. note::
        Although most of the times processes are more of one type than the other, it could have characteristics of both.

Prioritizing
^^^^^^^^^^^^

A common scheme for scheduling is based on the processes' priority. Higher priority processes are scheduled first, followed by a round-robin walk-through of the low-priority (if they equal value, of couse). The higher priority value might denote either preference in scheduling or longer timeslices.


Linux implements two separate disjoint priority values - ``nice`` and ``real-time priority``. The first one marks how nice a process is to others, or how willing it is to allow others to go first. It is a value in the range [-20; 20) and the higher the value, the lower the priority. The ``real-time priority`` on the other hand is a value in the range [0; 100); the higher the value, the higher the priority. Usually, real-time processes have bigger values.

Timeslices
^^^^^^^^^^

The CFS caculates timeslices in a unique way - instead of assigning actual values (i.e 10ms), it gives each process a proportion of the CPU based on the priority. Therefore, ``timeslice = f(load of the system)``. Moreover, the resulting proportion is mapped with the nice value of the process, which acts as a weight to it. Rather then choosing which process to run based on its priority, the CFS makes this decision relative to the evaluted proportion, where smaller value, means higher chance of being picked.

.. note:: 
        Timeslice may also be called *quantum* or *CPU slice*.

Desired Results of CFS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's look at an example: two processes executing in the system. One is highly interactive, thus - I/O bound (P), whilst the other is entirely CPU bound (Q). Since, we would like P to run smoothly from the user-perspective it should have high respond time, meaning it - low latency. Adversly, since Q is much more time consuming than P, we would not take into account latency introduced by the scheduling policy, which means that P should be more prioritized.

In the beginning, the CFS should give each of the two processes 50% of the CPU. However, P waits wait more time than executing, meaning that Q gets more CPU time. Taking all of this into account it is clear that since P runs way less than Q, it should get prioritized when it needs to, when it is being used (remember, it is an interactive process). Therefore, the CFS gives each process a **fair** execution policy.

Several problems exist in the above-described scheme with which the CFS has to deal with:

Problem #1
        If we try to map the nice value to a timeslice (or %), we end up with a problem. Let's say that there are two processes - one with 0 nice and one with 20 nice. Let's also say that 0 nice corresponds to a timeslice of 100ms. With this config, the scheduler will give the first process 100 out of 105 ms and 5ms to the second. However if two processes with 20 nice value exist, each of them would get 5ms. In reality this is 50% of the CPU, but this is inefficient since there should be a context switch each 5ms.

Problem #2
        Two processes - 0 and 1 nice values. Let's say that 0 nice corresponds to 100ms timeslice. This means that the first process gets 100ms and the second - 95ms, which is a 5% difference. If we change the nice-timeslice mapping, to ``0 nice -> 10ms``, the processes get 10ms and 5ms respectively, which is a 50% difference. This means that "nicing a process down" has very different effects depending on the mapping.

Problem #3
        An ability to assign absolute timeslices is desired in kernel time. This is a metric based on the period of the timer tick.
        **TODO: Revisit after Ch. 11 and fill**

Problem #4:
        Handling process after wake-up - we would to give a fresly woken up process a higher chance of being scheduled in order to improve interactiveness of I/O bound programs, but this might result in a unfair amount of CPU time.

Pseudo-solutions
        * Geomtric nice values (instead of arithmetic)
        * Decoupled measurement mapping timeslices to timer ticks

Actual problem
        Assigning absolute timeslices yields a constant switching rate, but variable scheduling fairness.

Completely Fair Scheduling Algorithm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since Linux is kinda complex, it allows different scheduling algorithms to coexist and actually operate coherently. This is implemented via *sheduling classes*, where ach class reprents a different algorithm. Each of them is assigned a priority value that is used when the base scheduler chooses which concrete scheduler to perform its algorithm at a given time (higher priority means higher chance of being picked). Among all scheduler classes, the CFS is set as default (``SCHED_NORMAL`` within the kernel).

Perfect Multitasking
        Rather then running two processes each for 5ms while utilizing 100% of the CPU, in an ideal perfect multitasking CPU we run them for 10ms and each of them gets 50% of the CPU.

This model is impractictal since it does not take switching costs in account.

Firstly, the base proportion is calcaulted - ``1 / n`` (where ``n`` is the total # of processes). Following that, instead of *assigning* a timeslice to each process based on the nice value, CFS uses it to *weight* the proportion of CPU each process receives.

Targeted latency
        Approximation of the "infinetely small" scheduling duration.

The actual timeslice is calculated according to the target latency - if two tasks with equal priority exist, each of them will execute for 10ms, if five tasks with equal priority exists, each of them will execute for 4 ms, etc.

Minimum granularity
        The minimum amount of time a process may execute. (By default - 1ms).

.. note::
        With higher number of process, the timeslice each of them gets decreases. This means that with infinte # of process, each one of them will get <something-close-to-0> ms. Therefore, *minimum granularity* is defined as a bare-minumim for each process to execute. However, as the # of processes increases, the fairness of the scheduler drops.

Revisit Problem #2
        With two processes (0 and 5 as nice values) and ``target latency = 20ms``, then they will get 15ms and 5ms timelices respectively. If, they have 10 and 15 as nice values, the timeslices are again 15ms and 5ms respectively.


Implementation
^^^^^^^^^^^^^^

.. code-block:: c
        :linenos:
        :emphasize-lines: 11

        // include/linux/sched.h

        struct sched_entity {
                struct load_weight	load;
                struct rb_node		run_node;
                struct list_head	group_node;
                unsigned int		on_rq;

                u64                     exec_start;
                u64			sum_exec_runtime;
                u64			vruntime;
                u64			prev_sum_exec_runtime;

                u64			last_wakeup;
                u64			avg_overlap;

                u64			nr_migrations;

                u64			start_runtime;
                u64			avg_wakeup;

                u64			avg_running;
                [...]
        };

Virtual runtime - ``vruntime``
        The actual time that the process spent running (weighted) in nanoseconds. This is used to approximate the "perfect multitasking CPU". In the ideal case it would not be useful, since all of the processes would have gotten the same amount of the CPU share. There is some accounting needed in order to keep it up-to-date. It is implemented in the ``update_curr()`` function.

.. code-block:: c
   :linenos:

   // kernel/sched_fair.c

   static void update_curr(struct cfs_rq *cfs_rq)
   {
	struct sched_entity *curr = cfs_rq->curr;
	u64 now = rq_of(cfs_rq)->clock;
	unsigned long delta_exec;

	if (unlikely(!curr))
		return;

	/*
	 * Get the amount of time the current task was running
	 * since the last time we changed load (this cannot
	 * overflow on 32 bits):
	 */
	delta_exec = (unsigned long)(now - curr->exec_start);
	if (!delta_exec)
		return;

	__update_curr(cfs_rq, curr, delta_exec);
	curr->exec_start = now;

	if (entity_is_task(curr)) {
		struct task_struct *curtask = task_of(curr);

		trace_sched_stat_runtime(curtask, delta_exec, curr->vruntime);
		cpuacct_charge(curtask, delta_exec);
		account_group_exec_runtime(curtask, delta_exec);
	}
    }


.. note::
        As far as I see, there has not been a huge change until now (5.14.7). The only notable difference is that the ``__update_curr()`` function has been removed and its body has been incorporated directly inside ``update_curr``.

The above function is called periodically both when a process becomes eligible for running and when it gets blocked. Therefore, the ``vruntime`` is accurate.
Therefore, it directly maps the fairness with which the process has been treated, the algorithm for picking the next process to schedule becomes - choose the process with lowest ``vruntime`` value. Furthermore, the list of runnable processes is organised in a ``rbtree`` in order to efficiently locate the one with minumim ``vruntime`` value, so the actual "pick-next-process" operation becomes "go left until nothing is left" :). If has not been simplified enough, a tree walk isn't even required since the leftmost element is cached in the CPU runqueue (see ``__pick_next_entity()``).

.. code-block:: c
        :linenos:

        // kernel/sched_fair.c

        static struct sched_entity *__pick_next_entity(struct cfs_rq *cfs_rq)
        {
                struct rb_node *left = cfs_rq->rb_leftmost;

                if (!left)
                        return NULL;

                return rb_entry(left, struct sched_entity, run_node);
        }

.. note::
        If ``NULL`` is returned from ``__pick_next_entity()``, there are no schedulable processes and the idle process is ran.

The functions which add processes in the red-black tree are named ``enqueue_entity()`` - updates statistics, and ``__enqueue_entity()`` - actual tree modification. This is the same function which caches the leftmost element. It gets executed when a process gets runnable. Logically, ``dequeue_entity()`` and ``__dequeue_entity()`` are those who handle the entity removing logic, when a process blocks or terminates.

The entry point of the scheduler is ``schedule()`` function. This is the abstract high-level routine which everybody calls when they need to "do something with the scheduler". The most interesting thing that happens is the ``pick_next_task()`` function call which selects the next scheduler class to operate.

Waiting and Waking-Up
^^^^^^^^^^^^^^^^^^^^^

Processor blocking is implemented the following way:

        1. The task marks itself as sleeping
        2. Puts itself in a wait-queue
        3. Removes itself from the red-black tree
        4. Calls ``schedule()`` to select new process

Waking-up is the opposite - runnable, removed from wait-queue and added to the red-black.

Waiting in the kernel is usually done in the following way:

.. code-block::
        :linenos:

        // q is the wait-queue, we wish to sleep on
        DEFINE_WAIT(wait);

        add_wait_queue(q, &wait);
        while (!condition) { // condition is the event that we are waiting for
                prepare_to_wait(&q, &wait, TASK_INTERRUPTIBLE);
                if (signal_pending(current)) {
                        // handle
                }

                schedule();
        }

        finish_wait(&wait);

