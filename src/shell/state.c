/* state.c: the resident shared state. */
#include "nm.h"

struct nm_state nm;
char nm_name[13];
char nm_lname[NM_LNAME_SIZE];

/* Handed to NextZXOS, so they must stay resident. */
const char nm_filter_sms[] = { '*', '.', 'S', 'M', 'S', 0xFF };
const char nm_filetypes[] = { 4, 'S', 'M', 'S', ':', 0xFF };
