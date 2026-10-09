/* far.c: the far-call trampoline. See docs/design.md, "Far calls". */
#include <arch/zxn.h>

#include "nm.h"

void *nm_far(uint8_t page, void *(*fn)(void *), void *arg)
{
    uint8_t old = ZXN_READ_REG(REG_MMU0 + 7);
    void *result;

    ZXN_WRITE_MMU7(page);
    result = fn(arg);
    ZXN_WRITE_MMU7(old);
    return result;
}
