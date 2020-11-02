#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/module.h>

#define MOD_AUTHOR "Kristiyan Stoimenov <kristoimenov@gmail.com>"
#define MOD_DESCRIPTION "A hello world kernel module"

MODULE_LICENSE("GPL");
MODULE_AUTHOR(MOD_AUTHOR);
MODULE_DESCRIPTION(MOD_DESCRIPTION);

static int __init hello_init(void) {
    printk(KERN_INFO "Hello kernel world\n");
    return 0;
}

static void __exit hello_exit(void) {
    printk(KERN_INFO "Bye kernel world\n");
}

module_init(hello_init);
module_exit(hello_exit);
