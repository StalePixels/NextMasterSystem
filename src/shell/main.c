/* main.c: the resident part of the shell. */
#include "nm.h"

/* A game's BREAK comes back through nm_resume (glue.asm) to here. */
void nm_run(void)
{
    for (;;) NM_FAR(PAGE_SESSION, session_pass, 0);
}

void main(void)
{
    NM_FAR(PAGE_SESSION, session_init, 0);
    if (nm.boot) nm.err = (uint8_t)(uintptr_t)NM_FAR(PAGE_LOADER, loader_load, 0);
    nm_run();
}
