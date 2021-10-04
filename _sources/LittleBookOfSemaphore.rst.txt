The Little Book Of Semaphores
=============================

Introduction
------------

Sequential
        Two events happen sequentially if we know the order of their execution

Concurrent
        Two events are concurrent if we cannot tell the order their execution by just looking at the program. We say that they are **non-deterministic**.


Semaphores
----------

*Def.:* Semaphore is a special integer with three special properties:

        * It may be initialized to any number, but after being constructed the only supported operatios are *increment* and *decrement*.
        * When decrementing, if the value drops below 0, the currently executing thread blocks and sleeps until another thread increments the semaphore.
        * When incrementing, if any threads are waiting on the semaphore, one of them gets unblocked.

What the semaphore's value represents?
        * If positive, then that is the number of threads that may decrement before blocking.
        * If negative, then the absolute value is the number of threads that are waiting on the semaphore.


**Operations**

=========    =========    ==============================
Up           Down         Meaning
=========    =========    ==============================
increment    decrement    What the operations do
---------    ---------    ------------------------------
signal       wait         What they are usually used for
---------    ---------    ------------------------------
V            P            Original names
=========    =========    ==============================

Some of the advantages of using semaphores over other synchronisation primitives include

        1)      They impose deliberate constraints
        2)      Clarity and organization
        3)      Efficient implementations


Basic Synchronisation Patterns
------------------------------

Signalling
^^^^^^^^^^


**Task: 2-Thread Randezvous**
For the following pseudo-code, guarantee that the execution order is `A1 < B2 && B1 < A2`:

.. code-block::

        // Thread A:
        [a1] ...
        [a2] ...

        // Thread B:
        [b1] ...
        [b2] ...

.. code-block::

        sem b1_done{0};
        sem a1_done{0};

        // ThreadA:
        [a1] ...
             b1_done.wait();
             a1_done.signal();
        [a2] ...

        // ThreadB:
        [b1] ...
             b1_done.signal();
             a1_done.wait();
        [b2] ...

**Task:**
Add mutual exclusion to following snipper:

.. code-block::

        // Thread A
        c++;

        // Thread B
        c++;

.. code-block::

        sem binsem{1};

        // Thread A
        binsem.wait();
        c++;
        binsem.signal();

        // Thread B
        binsem.wait();
        c++;
        binsem.signal();

**Task: Multiplex**
Enforce a limit on the amount thread that may execute concurrently in a critical section:

.. code-block::

        sem s{THREADS_NR};
        
        // Thread _
        s.wait();
        [...]
        s.signal();

**Task: Randezvous**
No thread may execute ``[critical section]`` before every one has executed ``[randezvous]``.

.. code-block::

        sem binsem{1};
        sem barrier{0};
        u32 count_reached{0};

        // Thread _
        [randezvous]
        binsem.wait();
        if (++count_reached >= NR_THREADS)
                barrier.signal();
        binsem.signal();

        barrier.wait();
        barrier.signal();
        [critical section]


.. note::
        The pattern of ``wait`` and ``signal`` in rapid succession is called **turnstile**.

.. warning::
        Common source of deadlocks - blocking on semaphore, while holding a mutex.

**Task: Auto-locking barrier (also called Two-phase barrier)**

.. code-block::

        sem binsem{1};
        sem turnstile_upper{1};
        sem turnstile_bottom{0};
        u32 count{0};

        binsem.wait();
                if (++count >= NR_THREADS)
                    turnstile_bottom.wait();
                    turnstile_upper.signal();
        binsem.signal();

        turnstile_upper.wait();         // first turnstile
        turnstile_upper.signal();

        binsem.wait();
                if (--count == 0)
                    turnstile_upper.wait();
                    turnstile_bottom.signal();
        binsem.signal();

        turnstile_bottom.wait();        // second turnstile
        turnstile_upper.signal();

**Preloaded barrier**

.. code-block::

        sem turnstile_bottom{1};
        sem turnstile_upper{0};
        sem binsem{1};
        u32 count{0};

        binsem.wait();
                if ++count >= NR_THREADS
                    turnstile_upper.signal(n);
        binsem.signal();

        turnstile_upper.wait();

        binsem.wait();
                if --count <= 0
                    turnstile_bottom.signal(n);
        binsem.signal();

        turnstile_bottom.wait();

**Task: Ballroom Dancers**

.. code-block::

        sem leaders{0};
        sem followers{0};
