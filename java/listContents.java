// File System related functions in Java

import java.io.*;
import java.util.*;


public class FileClass {
  public static void main (String[] args) throws IOException {
    File f = new File(args[0]);
    String[] dir = f.list();
    Arrays.sort(dir);
    for (int i = 0; i < dir.length; i++){
      System.out.println(dir[i]);
    }
  }
}
