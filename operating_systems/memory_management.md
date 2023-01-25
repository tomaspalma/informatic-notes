# 1. Segmentation

# 1.1. What is it?

# 1.2. Applications

Although it is normally said, at least in the Operating Systems course,
that segmentation is not used and that instead we use pagination, it is
**not** at all true.

There are some architectures, such as the *x86* one that use **both**.

Although, because of **portability issues**, it may be that the
operating systems use a more generic platform-independent approach and
do not create their own system having in mind just one architecture.
Otherwise, that would not be portable.

Instead, they usually probably create a more generic system that will
not rely on the architecture cpu to have that same support or
functioning.

# 2. Paginação
