# HMDSAniket
This is an implementation of a heterogeneous task scheduling algorithm: Heterogeneous Makespan-minimizing DAG Scheduler-Baseline (HMDS-Bl).
This HMDS-Bl is extended by employing a low-overhead depth-first branch and bound based search technique. This enhanced algorithm is HMDS (Heterogeneous Makespan-minimizing DAG Scheduler).
In future we will implement HMDS as well.

HMDS Link --> https://dl.acm.org/doi/10.1145/3477037?sid=SCITRUS

There are three files:
setup.py
pft_rank.py
HMDS_Bl.py

setup.py --> deals with inputs of various requirements, organizing tasks into a Directed Acyclic Graph, and finding predecessors and successors of various      tasks.

pft_rank --> returns PFT (Predicted Finish Time) and rank (which is average of PFTs on all processors).
             PFT is a 2D matrix of form |V| X |P|
             rank is a list of length |V|
             
HMDS_Bl.py --> uses PFT and rank.
               sort tasks in non-increasing order of rank.
               get each task
               compute EST, EFT, O_eft
               EST --> Effective Start Time --> of form |V| X |P|
               EFT --> Effective Finish Time --> of form |V| X |P|
               O_eft --> Estimate of Sink Task's completion time (T_Exit completion time) relative to the EFTof current task on a particular processor. --> of form |V| X |P|.
               find Processor pn with minimum O_eft.
               assign that task to the processor pn.
