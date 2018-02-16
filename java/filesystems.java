// File System related functions in Java

import java.io.*;
import java.util.*;


public class FileClass {
  public static void main (String[] args) throws IOException {
    File f = new File(args[0]);

    /* See if file exists */
    if (f.exists()) {
      System.out.println("file found");
    } else {
      System.out.print("file not found");
    }
    /* Check if the file is readable */
    if (f.canRead()) {
      System.out.println("file is readable");
    } else {
      System.out.print("file not readable");
    }
    /* Check if the file is writeable */
    if (f.canWrite()) {
      System.out.println("file is writeable");
    } else {
      System.out.print("file not writeable");
    }

    Date d = new Date();
    d.setTime(f.lastModified());
    System.out.println("Last modified" + d);

    if (f.isFile()) {
      System.out.println("File size is " + f.length() + " bytes.");
    } else if (f.isDirectory()) {
      System.out.println("This is a directory");
    } else {
      System.out.println("Neither a file nor a directory");
    }
  }
}
