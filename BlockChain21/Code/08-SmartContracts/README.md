# Blockchain21: *Blockchain* #
### Academic year 2021/22 ###

## Code for smart (stateful) constracts ##

We create a simple smart contract that exemplifies the use of global and local state.
Specifically, the contract maintains one global counter ```gcnt1``` (incremented by 1 at each invocation)
and one local variable ```lcnt1``` (incremented by 7 at each invocation).

### Step by step ###

1. Create the approval file [01-class.teal](01-class.teal)
2. Run [createApp.py](createApp.py) to create the application.
    It takes three command line arguments: the filename containing the mnemonic of the creator account,
        the filename containing the teal program, the directory of the node.
    Take note of the application index that will be needed for the following steps.

    Note that you must use the creator address in the approval program. Currently the teal file  has the address
    that I have used during my lecture.

2. Run [optinApp.py](optinApp.py) to allow addresses to opt in the contract. 
    It takes three command line arguments: the filename containing the mnemonic of the address
    that wishes to opt in, the application index, and the directory of the node.
    
3. Run [callApp.py](callApp.py) to allow addresses to opt in the contract. 
    It takes three command line arguments: the filename containing the mnemonic of the address
    that wishes to opt in, the application index, and the directory of the node.
    
    The output shows the current values of the counters.
    The global and local counter can be obtained from the ```response``` returned by the transaction once it 
    has completed (in the fields ```global-state-delta``` and ```local-state-delta```, respectively).
    Note that only variables whose value have changed are reported (whence the ```delta```).

    Alternatively, the local state can be obtained from the field ```apps-local-state``` of the 
    ```account_info``` obtained from the node about the address that has called the application.

    The global state can also be obtained from the script ```readGlobalValues.py``` that accesses 
    the ```account_info``` of the creator of the application.
