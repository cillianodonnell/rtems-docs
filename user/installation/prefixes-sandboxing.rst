.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. comment: Copyright (c) 2016 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

.. _prefixes:

Prefixes
========

.. index:: Prefixes

You will see the term :ref:term:`prefix` referred to thoughout this
documentation and in a wide number of software packages you can download from
the internet. A **prefix** is the path on your computer a software package is
built and installed under. Packages that have a **prefix** will place all parts
under the **prefix** path. On a host computer like Linux the packages you
install from your distribution typically use a platform specific standard
**prefix**. For example on Linux it is :file:`/usr` and on FreeBSD it is
:file:`/usr/local`.

We recommend you *DO NOT* use the standard **prefix** when installing the RTEMS
Tools. The standard **prefix** is the default **prefix** each package built by
the RSB contains. If you are building the tools when logged in as a *Standard
User* and not as the *Super User* (``root``) or *Administrator* the RTEMS
Source Builder (RSB) *will* fail and report an error if the default **prefix**
is not writable. We recommend you leave the standand **prefix** for the
packages your operating system installs or software you manually install such
as applications.

A further reason not to use the standard **prefix** is to allow more than one
version of RTEMS to exist on your host machine at a time. The ``autoconf`` and
``automake`` tools required by RTEMS are not versioned and vary between the
various versions of RTEMS. If you use a single **prefix** such as the standard
**prefix** there is a chance parts from a package of different versions may
interact. This should not happen but it can.

For POSIX or Unix hosts, the RTEMS Project uses :file:`/opt/rtems` as it's
standard **prefix**. We view this **prefix** as a production level path, and we
prefer to place development versions under a different **prefix** away from the
production versions. Under this top level **prefix** we place the various
versions we need for development. For example the version 4.11.0 **prefix**
would be :file:`/opt/rtems/4.11.0`. If an update called 4.11.1 is released the
**prefix** would be :file:`/opt/rtems/4.11.1`. These are recommendations and
the choice of what you use is entirely yours. You may decide to have a single
path for all RTEMS 4.11 releases of :file:`/opt/rtems/4.11`.

For Windows a typical **prefix** is :file:`C:\\opt\\rtems` and as an MSYS2 path
this is :file:`/c/opt/rtems`.

.. _project-sandboxing:

Project Sandboxing
------------------

Project specific sandboxes let you have a number of projects running in
parallel with each project in its own sandbox. You simply have a
:ref:term:`prefix` per project and under that prefix you create a simple yet
repeatable structure.

As an example lets say I have a large disk mounted under :file:`/bd` for *Big
Disk*. As ``root`` create a directory called ``projects`` and give the
directory suitable permissions to be writable by you as a user.

Lets create a project sandbox for my *Box Sorter* project. First create a
project directory called :file:`/bd/projects/box-sorter`. Under this create
:file:`rtems` and under that create :file:`rtems-4.11.0`. Under this path you
can follow the :ref:`released-version` procedure to build a tool set using the
prefix of :file:`/bd/projects/box-sorter/rtems/4.11.0`. You are free to create
your project specific directories under :file:`/bd/projects/box-sorter`. The
top level directories would be:

:file:`/bd/projects`
  Project specific development trees.

:file:`/bd/projects/box-sorter`
  Box Sorter project sandbox.

:file:`/bd/projects/box-sorter/rtems/4.11.0`
  Project prefix for RTEMS 4.11.0 compiler, debuggers, tools and installed
  Board Support Package (BSP).

A variation is to use the ``--without-rtems`` option with the RSB to not build
the BSPs when building the tools and to build RTEMS specifically for each
project. This lets you have a production tools installed at a top level on your
disk and each project can have a specific and possibly customised version of
RTEMS. The top level directories would be:

:file:`/bd/rtems`
  The top path to production tools.

:file:`/bd/rtems/4.11.0`
  Production prefix for RTEMS 4.11.0 compiler, debuggers and tools.

:file:`/bd/projects`
  Project specific development trees.

:file:`/bd/projects/box-sorter`
  Box Sorter project sandbox.

:file:`/bd/projects/box-sorter/rtems`
  Box Sorter project's custom RTEMS kernel source and installed BSP.

A further varation if there is an RTEMS kernel you want to share between
projects is it to move this to a top level and share. In this case you will end
up with:

:file:`/bd/rtems`
  The top path to production tools and kernels.

:file:`/bd/rtems/4.11.0`
  Production prefix for RTEMS 4.11.0.

:file:`/bd/rtems/4.11.0/tools`
  Production prefix for RTEMS 4.11.0 compiler, debuggers and tools.

:file:`/bd/rtems/4.11.0/bsps`
  Production prefix for RTEMS 4.11.0 Board Support Packages (BSPs).

:file:`/bd/projects`
  Project specific development trees.

:file:`/bd/projects/box-sorter`
  Box Sorter project sandbox.

Finally you can have a single set of *production* tools and RTEMS BSPs on the
disk under :file:`/bd/rtems` you can share between your projects. The top level
directories would be:

:file:`/bd/rtems`
  The top path to production tools and kernels.

:file:`/bd/rtems/4.11.0`
  Production prefix for RTEMS 4.11.0 compiler, debuggers, tools and Board
  Support Packages (BSPs).

:file:`/bd/projects`
  Project specific development trees.

:file:`/bd/projects/box-sorter`
  Box Sorter project sandbox.

The project sandoxing approach allows you move a specific production part into
the project's sandbox to allow you to customise it. This is useful if you are
testing new releases. The typical dependency is the order listed above. You can
test new RTEMS kernels with production tools but new tools will require you
build the kernel with them. Release notes with each release will let know
what you need to update.

If the machine is a central project development machine simply replace
:file:`projects` with :file:`users` and give each user a personal directory.
