import machines

machines.machinesFun() # Hello from Machines Module
machines.machinesDoWorkFun() # Machines Do Work

import machines as mac

mac.machinesFun() # Hello from Machines Module
mac.machinesDoWorkFun() # Machines Do Work

from machines import machinesDoWorkFun

machinesFun() # Error
machinesDoWorkFun() # Machines Do Work

from machines import *

machinesFun() # Hello from Machines Module
machinesDoWorkFun() # Machines Do Work

# ================================== Packages ==================================

import Workers.labourerWorkers

Workers.labourerWorkers.labourerWorkersFun() # Hello from Lobourer Workers Module

from Workers.labourerWorkers import labourerWorkersFun

labourerWorkersFun() # Hello from Lobourer Workers Module

from Workers import labourerWorkers

labourerWorkers.labourerWorkersFun() # Hello from Lobourer Workers Module

import Workers.Managers.hiringManagers

Workers.Managers.hiringManagers.hiringManagersFun() # Hello from Hiring Managers Module

from Workers.Managers.hiringManagers import hiringManagersFun

hiringManagersFun() # Hello from Hiring Managers Module

from Workers.Managers import hiringManagers

hiringManagers.hiringManagersFun() # Hello from Hiring Managers Module