import java.io.IOException;
import java.io.File;
import java.io.FileWriter;
import java.util.function.Consumer;

public class Main {
    public static void main(String[] args) {
      int n = 1000;
      int step = 10;
      BenchMark.plot_sort(SortingAlgorithms::insertion_sort,
                          "insertion",
                          n,
                          step);
      BenchMark.plot_sort(SortingAlgorithms::heap_sort,
                          "heap",
                          n,
                          step);
    }
  }

class BenchMark
{
  static void plot_sort(Consumer<int[]> func, String name, int max, int step)
  {
    String fileName = "java-" + name + ".csv";
    init_csv(fileName);
    for (int i = 1; i<=max; i+=step)
    {
      int[] nums = createArray(i);
      long startTime = System.nanoTime();
      func.accept(nums);
      long endTime = System.nanoTime();
      double deltaTime = (double) (endTime - startTime)/1000000000; // dividingon one billion to get seconds
      append_to_csv(fileName, nums.length, deltaTime);
    }

  }
  static int[] createArray(int i)
  {
    int[] nums = new int[i];

    for (int j = 0; j < i; j++) {
        nums[j] = i - j;
    }
    return nums;
  }


  static void init_csv(String fileName)
  {
    try 
    {
      File fileObj = new File(fileName);
      fileObj.createNewFile(); // create new file if needed
      FileWriter fileWriter = new FileWriter(fileName);
      fileWriter.write("n,time\n");
      fileWriter.close();



    }
    catch (IOException e)
    {
      System.out.println("An error occured.");
      e.printStackTrace();
    }
  }

  static void append_to_csv(String fileName, int n, double deltaTime)
  {
    try
    {
      FileWriter fileWriter = new FileWriter(fileName, true);
      fileWriter.write(String.valueOf(n) + "," + String.valueOf(deltaTime) + "\n");
      fileWriter.close();
    }
    catch (IOException e)
    {
      System.out.println("An error occured while trying to append to file");
      e.printStackTrace();
    }
  }

}
