---
title: SLURM notes
slug: slurm-notes
date: 2017-06-22 10:38
category: slurm
tags: slurm, hpc
---

SLURM is an open-source resource manager designed for Linux clusters of all sizes. It provides three key functions:

1. Allocates exclusive and/or non-exclusive access to resources (computer nodes) to users so they can perform work.
2. Provides a framework for starting, executing and monitoring work on a set of allocated nodes.
3. Arbitrates contention for resources by managing a queue of pending work.

Use of optional plugins provides the functionality needed to satisfy the needs of demanding HPC centers. More complex configurations rely upon a database for archiving accounting records, managing resource limits by user or bank account, and supporting sophisticated scheduling algorithms.

#### SchedMD
SchedMD is the core company behind the Slurm workload manager software, a free open-source workload manager designed specifically to satisfy the demanding needs of high performance computing. Slurm is in widespread use at government laboratories, universities and companies world wide. As of the November 2014 Top 500 computer list, Slurm was performing workload management on six of the ten most powerful computers in the world including the number 1 system, Tianhe-2 with 3,120,000 computing cores.

SchedMD performs most Slurm development, reviews and integrates contributions from others, distributes and maintains the canonical version of Slurm. SchedMD also provides training, installation, configuration, custom development and support (including joint Slurm support with Bull, Cray and Science+Computing).

### Fundamental principles at play during the lifecycle of a job managed by SLURM:%
* **Allocation**: How, when, and why SLURM allocates resources for a job.
* **Execution**: What SLURM runs on allocated resources, and how.
* **Security**: Allowed acccess to allocated resources, and how this is achieved.

#### Allocation

There are three commands in SLURM that can allocate resources to a job under appropriate conditions: `srun`, `sbatch`, and `salloc`. They all accept the same set of command line options with respect to resource allocation. On Stampede, the resources that SLURM allocates to a job are whole compute nodes. All nodes on a partition (queue) on Stampede are identical. When a job is submitted to Stampede, the SLURM scheduler calculates and allocates the minimum number of whole compute nodes that will be able to satisfy the job.

**Allocation Parameters**:

SLURM provides a variety of command line parameters `srun`, `sbatch`, and `salloc` for specifying the allocation. On Stampede, partly because it allocates identical whole nodes within a single partition, the most relevant parameters for allocation are nodes (-N) and tasks (-n). Hence, the selection of a particular partition strictly determines the hardware capability of the allocated nodes. Advanced options, such as requesting allocations with specific hardware features, are not supported.

**Allocation Method**:

`salloc`, `sbatch`, and `srun` differ in the way they allocate and release nodes

`sbatch` always creates a new resource allocation when it is invoked, executes a job script on one of the allocated nodes (master node), then releases the allocation once the script terminates. An additional feature of sbatch is that it will parse this script at job submission time for lines that begin with #SBATCH and contain sbath options in lieu of command line arguments. Command line arguments override the same #SBATCH options in the script, so a single batch script can be invoked for different task-sized allocations by specifying -N or -n options on the command line when submitting a job script withsbatch

`srun` may or may not create an allocation, depending on how it is invoked. If it is invoked on the command line of a login node, then it will create a new allocation and execute the command following srun. If it is invoked in a batch script (a use case that is disallowed on Stampede), it will simply run a task on the current allocation. Likewise, srun may be given a --jobid argument that tells it to run the task as part of the given job, on the specified job's own allocation.

`salloc` always creates a new resource allocation when it is invoked, but doesn't necessarily run any tasks on the allocated nodes. The typical use case of salloc is to create an allocation in order to run a series of subsequent srun commands either through an interactive bash session, or a script which runs from the login node. It releases the allocation after the script or bash session terminates. This use case is not supported on Stampede, so salloc is of limited use there.

#### Execution

The `sbatch` and `srun` commands are used to execute tasks on allocated nodes. They differ significantly in how, where, and when they execute tasks, but the tasks they do run execute in similar environments.

`sbatch` is a means of asynchronously submitting a batch file (from which tasks will be executed) to execute on allocated resources. It is inherently asynchronous in the sense that it simply queues a script to be run on allocated resources at some point in the future, and returns success once the job has been successfully queued. The sequence of events is:

The user submits a script via sbatch for later execution.
This script must be a text file that begins with a shebang (#!) line specifying the absolute path to an interpreter for the script.
The interpreter may be any executable, e.g. /bin/bash, /usr/bin/perl, /usr/bin/python. [TACC] recommends using /bin/bash or /bin/csh as the interpreter (not /bin/sh) to ensure that the module command is automatically defined and a suitable environment is available to ibrun. Using an interpreter like perl and python may require extra work to load modules within the submission script.
When resources become available, they are allocated to this job.
The script is executed on one node (the master node).
It is the script's responsibility to launch any other tasks on the nodes allocated on the job.
stdout and stderr from the script are captured by SLURM and redirected to output file(s).
When the script terminates, the allocation is released.
The script may choose to exit with a return code. SLURM will interpret a nonzero return code as a failure.

`srun` is a means of synchronously submitting a single command to run in parallel on a new or existing allocation. It is inherently synchronous because it attempts to launch tasks on an allocated resource, waits (blocks) until these resources are available, and returns only when the tasks have completed. On Stampede, the most common use of srun is to start an interactive session on one or more compute nodes, as in:

```bash
srun ‑‑pty ‑A acct ‑p queue ‑t hh:mm:ss ‑n tasks ‑N nodes /bin/bash ‑l
```

The sequence of events is as follows:

The user submits a command for execution on an allocation
This command may include command line arguments
It will be executed exactly as specified on one or more compute nodes in the allocation
If an allocation already exists, it will run right away. Otherwise, it will block until a new allocation has been established
For `srun` to run in an existing allocation, its arguments must specify an existing job, and must be compatible with that job (e.g. same partition, number of tasks can fit within existing allocation, etc.).
n identical copies of the command are run simultaneously on the allocated resources as individual tasks. stdout and sterr for these tasks is redirected to srun's own stdout and stderr.
If the --pty argument is used, srun will run in pseudo terminal mode and direct input and output to the user's shell. This is how interactive mode is run: use srun to run a shell (/bin/bash command) on an allocated node, and connect your terminal to its input and output.
The number and distribution of tasks is determined by the -N and -n command line options, as well as options such as -w which can be used to manually enumerate the nodes within the allocation on which to run the tasks.
On Stampede, because SLURM does not use the MPI plugin, these tasks are simply n identical copies of the same command and will not be launched in an MPI environment. As will be seen in a later section, this method of launching tasks can be used to implement parameter sweeps using serial or threaded code.
When all tasks terminate, the invocation of `srun` will exit. If srun was used to create the allocation, then the allocation will be released and the job ended. Otherwise, the allocation will remain.

#### Security

Aside from scheduling and queuing jobs from multiple users in order to fairly divide work among the compute nodes on Stampede, SLURM provides additional measures to assure that jobs and users do not interfere with one another. Perhaps the most useful to understand are features related to ssh access of compute nodes, networking, and job cleanup.

**SSH Access**:

SLURM provides an optional Pluggable Authentication Module (PAM) to allow logins to compute nodes under certain circumstances. This allows Stampede to implement policies allowing users to ssh into nodes involved in their own jobs, while denying access to nodes allocated to other users. In other words, if you attempt to ssh into a random compute node, you will be denied. If you attempt to ssh into compute nodes (or to attached MICs when running in the MIC-specific partitions) that are running your job, you will succeed.

SSH can be a useful tool for interacting with running jobs. When invoked from within a batch script, ssh can be used to execute commands on particular nodes within the allocation. Tools such as the TACC launcher are based on this principle. Likewise, it is possible to manually ssh into allocated nodes to access the node in an interactive shell. This can be useful for inspecting the state of a node running a job (e.g. with the top utility). CPU usage, I/O waiting, and other characteristics can be quickly and informally observed this way.

**Job Cleanup**:

After a job completes, SLURM may be configured to clean up each node of the allocation by running an epilog script as root. Stampede leverages this ability to clean up the /tmp storage on a node and running processes once a job terminates. Any processes owned by the user will be terminated (even those not directly initiated by SLURM, including independent ssh sessions described above).

**Networking**:

While ssh access is restricted via the PAM module, arbitrary communication ports opened by applications running as part of your job are not influenced by SLURM. In this case, security is entirely up to the application able to accept connections. VNC is a common example of the use of a connection. As a result, Stampede compute nodes do not allow network connections to the outside world. If it is necessary to connect to a compute node from outside Stampede, SSH tunneling between the login node and compute node must be used.

### Job Submission

This section describes several advanced job submission techniques having different characteristics. These submission techniques are largely independent from the runtime environment they create, so each of these techniques may be used with different runtimes to achieve different effects.

SLURM offers a dependency mechanism that allows conditional execution of a job based upon some characteristic of the execution of another job. If a job is specified as being dependent on another, that job is blocked in the queue until the dependency condition is achieved. The job executes or is cancelled based on evaluating this condition. Through dependencies, control flow between jobs can be established.

#### Dependency Conditions

* **after**: Indicates that the job may begin after the dependent job(s) have started executing. Using this, jobs may be ordered with respect to their starting times.

* **afterany**: Indicates that the job may begin after the dependent job(s) have terminated, regardless of how they were terminated (e.g. success, failure, cancellation).

* **afterok**: Indicates that the job may begin after the dependent job(s) have run to completion successfully with an exit code of 0.

* **afternotok**: Indicates that a job may begin after the dependent jobs(s) have terminated, and at least one of the jobs has failed (return code > 0) or terminated abnormally.

* **expand**: Indicates that a job will execute with the resources allocated to the dependent job, plus any additional resources allocated to the current job. Only one job may be specified with an expand dependency - a job cannot expand the resources allocated to multiple jobs.

* **singleton**: This assures that only one job with the same name and user executes at a given time. If any job with the same name is executing, the current job will block until these job(s) terminate for any reason.

For those dependencies that accept job IDs as an argument (all except 'singleton'), a list of job IDs may be provided as a colon separated list. For example --dependency=afterok:100:101:102:103:104:105 indicates that the job shall start only after jobs 100-105 successfully complete.
