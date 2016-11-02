RTEMS Project Documentation
===========================

The documents is written in ReST and built using Sphinx. The build system will
check the version and ensure you have a suitable version. If your host does not
provide a packaged version use PIP to fetch a recent version. The Sphinx
website provides details on doing this.

Building PDF requires a full Latex install.

Building
--------

To build enter in the top directory:

  $ ./waf configure
  $ ./waf

PDF output can be built without needing to configure again:

  $ ./waf --pdf

To build and install to a specific location:

  $ ./waf configure --prefix=/foo/my/location
  $ ./waf build install

If you need to debug what is happening use configure with a suitable Sphinx
version level:

  $ ./waf configure --sphinx-verbose=-v
  $ ./waf clean build

Documentation Standard
----------------------

This following details the documentation standard. If in doubt first search the
existing documentation for an example and if unsure ask.

1. All text is to be formatted to wrap at 80 columns. Do not manually line feed
   before 80.

2. Pasted text such as console output can exceed 80 columns however it is
   preferred even this text is wrapped at 80 columns. Long lines in code block
   text causes issues with the PDF output.

3. For pasted output, shell commands and code use '.. code-block::' with
   'c' for C code and 'shell' for shell code and terminal output. If you need
   line number use:

    .. code-block:: shell
       :linenos:

4. Use the directives for 'note', 'warning', and 'topic'. Do not add 'TIP',
   'Important' or 'Warning' to the text. Let the mark-up language handle
   this. The supported directives are:

     .. warning::
     .. note::
     .. topic::

   These directives reference specific CSS sytle support.

5. Images are placed in the 'images' directory. Do not place images in the
   source directories. Using a common 'images' tree of images promotes sharing
   of images. To add an image use:

    .. figure:: ../images/my-image.png
       :wdith: 75%
       :align: center
       :alt: This is the alt text for some output types.

6. Callouts can be implement manually using a code block and a topic block. For
   example:

     .. code-block: c

        #include <stdio.h>                             <1>
        int main(int argc, char** argv)                <2>
        {
           printf("Hello world\n");                    <3>
           return 0;                                   <4>
        }

     .. topic:: Items:

       1. Include the standard input/output header file.

       2. The program starts here.

       3. Print something to the standard output device.

       4. Exit with an exit code of 0. This is value can be checked by the
          caller of this program.

   Note, the topic items are manually number. This makes is easier to see which
   item matches the text. Use <> for the number and try to align to column
   76. If there is more than 9 items align to column 75. Use haning indents if
   an items extends over a single line.

7. Use the RTEMS domain references for URLs and mailing lists. For example to
   insert the RTEMS developers list use:

     :r:list:`devel`
     :r:url:`git`

   The valid lists are:

     announce     : Announce Mailing List
     bugs         : Bugs Mailing List
     devel        : Developers Mailing List
     build        : Build Logs
     users        : Users Mailing List
     vc           : Version Control Mailing List

  The valif URLs are:

     trac         : https://devel.rtems.org/
     devel        : https://devel.rtems.org/
     www          : https://www.rtems.org/
     buildbot     : https://buildbot.rtems.org/
     builder      : https://builder.rtems.org/
     docs         : https://docs.rtems.org/
     lists        : https://lists.rtems.org/
     git          : https://git.rtems.org/
     ftp          : https://ftp.rtems.org/
     review       : https://review.rtems.org/
     bugs         : https://devel.rtems.org/wiki/Bugs/
     gsoc         : https://devel.rtems.org/wiki/GSoC/
     socis        : https://devel.rtems.org/wiki/SOCIS/