#define NumINP 3
#define NumGates 5
Gate circuit[]={{0,0,0,0,{0,0},{3,0},"OR", orGate,{8,8},
                    {{(unsigned char *)NULL,(unsigned char *)NULL},
                     {(unsigned char *)NULL,(unsigned char *)NULL}},
                     {(unsigned char *)NULL,(unsigned char *)NULL}
                    },
                    {1,0,1,1,{0,0},{3,1},"AND", andGate,{8,8},
                    {{(unsigned char *)NULL,(unsigned char *)NULL},
                     {(unsigned char *)NULL,(unsigned char *)NULL}},
                     {(unsigned char *)NULL,(unsigned char *)NULL}
                    },
                    {2,0,2,2,{0,0},{4,1},"OR",  orGate,{9,9},
                    {{(unsigned char *)NULL,(unsigned char *)NULL},
                     {(unsigned char *)NULL,(unsigned char *)NULL}},
                     {(unsigned char *)NULL,(unsigned char *)NULL}
                    },
                    {3,1,1,1,{0,1},{4,0},"OR",  orGate,{8,8},
                    {{(unsigned char *)NULL,(unsigned char *)NULL},
                     {(unsigned char *)NULL,(unsigned char *)NULL}},
                     {(unsigned char *)NULL,(unsigned char *)NULL}
                    },
                    {4,2,1,1,{3,2},{8,4},"AND", andGate,{8,8},
                    {{(unsigned char *)NULL,(unsigned char *)NULL},
                     {(unsigned char *)NULL,(unsigned char *)NULL}},
                     {(unsigned char *)NULL,(unsigned char *)NULL}
                    },
                };


