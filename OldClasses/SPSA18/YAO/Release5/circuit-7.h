#define NumINP 4
#define NumGates 7
Gate circuit[]={    {0,0,0,0,{0,0},{4,0},"NOR", xorGate,{8,8},
                    {{(unsigned char *)NULL,(unsigned char *)NULL},
                     {(unsigned char *)NULL,(unsigned char *)NULL}},
                     {(unsigned char *)NULL,(unsigned char *)NULL}
                    },
                    {1,0,1,1,{0,0},{4,1},"AND", andGate,{8,8},
                    {{(unsigned char *)NULL,(unsigned char *)NULL},
                     {(unsigned char *)NULL,(unsigned char *)NULL}},
                     {(unsigned char *)NULL,(unsigned char *)NULL}
                    },
                    {2,0,2,2,{0,0},{5,0},"OR",  orGate,{9,9},
                    {{(unsigned char *)NULL,(unsigned char *)NULL},
                     {(unsigned char *)NULL,(unsigned char *)NULL}},
                     {(unsigned char *)NULL,(unsigned char *)NULL}
                    },
                    {3,0,3,3,{0,1},{5,1},"NOR",  norGate,{8,8},
                    {{(unsigned char *)NULL,(unsigned char *)NULL},
                     {(unsigned char *)NULL,(unsigned char *)NULL}},
                     {(unsigned char *)NULL,(unsigned char *)NULL}
                    },
                    {4,1,9,9,{0,1},{6,0},"NAND", nandGate,{8,8},
                    {{(unsigned char *)NULL,(unsigned char *)NULL},
                     {(unsigned char *)NULL,(unsigned char *)NULL}},
                     {(unsigned char *)NULL,(unsigned char *)NULL}
                    },
                    {5,1,9,9,{2,3},{6,1},"AND", andGate,{8,8},
                    {{(unsigned char *)NULL,(unsigned char *)NULL},
                     {(unsigned char *)NULL,(unsigned char *)NULL}},
                     {(unsigned char *)NULL,(unsigned char *)NULL}
                    },
                    {6,2,9,9,{4,5},{9,9},"NOR", xorGate,{8,8},
                    {{(unsigned char *)NULL,(unsigned char *)NULL},
                     {(unsigned char *)NULL,(unsigned char *)NULL}},
                     {(unsigned char *)NULL,(unsigned char *)NULL}
                    },
                };

