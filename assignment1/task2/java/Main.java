import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
      int[] test = {1, 2, 3};
      SortingAlgorithms.heap_sort();
      SortingAlgorithms.insertion_sort(test);
      System.out.println(Arrays.toString(test));
    }
  }
