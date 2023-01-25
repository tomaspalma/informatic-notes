# 1. Versions compatibility with the linux kernel

When we build a module, it is built against a certain version of the
linux source tree.

If, for example, we try to load a kernel module that was built with the
source tree for kernel version 5.10 in a system with 6.2 we are not
going to be able to load the module.

**How exactly is this check done?**

The module we try to load (the object file) is linked against another
file called *vermagic.o*, with which we will be able to check the kernel
version of the current running kernel and the one that the module was
compiled with.

**What is the error that is given when there is a version mismatch?**

    linux@pc ~ $ insmod module.ko
    Error inserting './module.ko': -1 Invalid module format
