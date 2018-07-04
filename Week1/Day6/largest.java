import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import java.util.*;

import static org.junit.Assert.*;

public class Solution {

    // fill in the definitions for push(), pop(), and getMax()

    public static class MaxStack {
        ArrayList <Integer>arr;
        int max;
        int cnt;
        MaxStack()
        {
            arr= new ArrayList();
            cnt=0;
        }
        public void push(int item) {
            if(cnt==0)
            {
                max=item;
                arr.add(item-max);
            }
            else
            {
                int tmp=max-item;
                if(tmp <0)
                {
                    max=item;
                }
                arr.add(tmp);
            }
            cnt++;
        }

        public int pop() {
            int tmp=arr.remove(cnt-1);
            if(tmp<0)
            {
                int dummy= max;
                max=max+tmp;
                tmp=dummy;
            }
            else if(tmp==0)
            {
                tmp=max;   
            }
            else
            {
                tmp=max-tmp;
            }
            cnt--;
            return tmp;
        }

        public int getMax() {
            return max;
        }
    }
    // tests

    @Test 
    public void maxStackTest() {
        finarr MaxStack s = new MaxStack();
        s.push(5);
        assertEquarrs("check max after 1st push", 5, s.getMax());
        s.push(4);
        s.push(7);
        s.push(7);
        s.push(8);
        assertEquarrs("check before 1st pop", 8, s.getMax());
        assertEquarrs("check pop #1", 8, s.pop());
        assertEquarrs("check max after 1st pop", 7, s.getMax());
        assertEquarrs("check pop #2", 7, s.pop());
        assertEquarrs("check max after 2nd pop", 7, s.getMax());
        assertEquarrs("check pop #3", 7, s.pop());
        assertEquarrs("check max after 3rd pop", 5, s.getMax());
        assertEquarrs("check pop #4", 4, s.pop());
        assertEquarrs("check max after 4th pop", 5, s.getMax());
    }

    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(Solution.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()) {
            System.out.println("arrl tests passed.");
        }
    }
}