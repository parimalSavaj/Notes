## pattern 01

![](./img/pattern%2001.png)

> `plan`

no plan need.

> `code`

```java
import java.util.Scanner;

public class pattern01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print("*");
            }
            System.out.println("*");
        }
    }
}
```

---

## pattern 02

![](./img/pattern%2002.png)

> `plan`

no plan need.

> `code`

```java
import java.util.Scanner;

public class pattern02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter n value: ");
        int n = sc.nextInt();

        for(int i = 0; i < n; i++){
            for(int j = 0; j <= i; j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
```

---

## pattern 03

![](./img/pattern%2003.png)

> `plan`

no need.

> `code`

```java
import java.util.Scanner;

public class pattern03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter n value: ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print(j + 1);
            }
            System.out.println();
        }
    }
}
```

---

## pattern 04

![](./img/pattern%2004.png)

> `plan`

no need.

> `code`

```java
import java.util.Scanner;

public class pattern04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter n value: ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print(i + 1);
            }
            System.out.println();
        }
    }
}
```

---

## pattern 05

![](./img/pattern%2005.png)

> `plan`

outer loop start from n.

> `code`

```java
import java.util.Scanner;

public class pattern05 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter n value : ");
        int n = sc.nextInt();

        for(int i = n; i > 0; i--){
            for(int j = 0; j < i; j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
```

---

## pattern 06

![](./img/pattern%2006.png)

> `plan`

outer loop start with n.

> `code`

```java
import java.util.Scanner;

public class pattern06 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for(int i = n; i > 0; i--){
            for(int j = 0; j < i; j++){
                System.out.print(j + 1);
            }
            System.out.println();
        }
    }
}
```

---

## pattern 07

![](./img/pattern%2007.png)

> `plan`

- formula space star

- calculation

| space | star |
| ----- | ---- |
| 4     | 1    |
| 3     | 3    |
| 2     | 5    |
| 1     | 7    |
| 0     | 9    |

> `code`

```java
import java.util.Scanner;

public class pattern07 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter n value: ");
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            // space
            for (int j = i; j < n; j++) {
                System.out.print(" ");
            }

            // star
            for (int j = 1; j < i * 2; j++) {
                System.out.print("*");
            }

            System.out.println();
        }
    }
}
```

---

## pattern 08

![](./img/pattern%2008.png)

> `plan`

- formula space star

- calculation

| space | star |
| ----- | ---- |
| 0     | 9    |
| 1     | 7    |
| 2     | 5    |
| 3     | 3    |
| 4     | 1    |

> `code`

```java
import java.util.Scanner;

public class pattern08 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for (int i = n; i > 0; i--) {
            // space
            for (int j = i; j < n; j++) {
                System.out.print(" ");
            }

            // star
            for (int j = 1; j < i * 2; j++) {
                System.out.print("*");
            }

            System.out.println();
        }
    }
}
```

---

## pattern 09

![](./img/pattern%2009.png)

> `plan`

- combination of pattern 7 and 8.

> `code`

```java
import java.util.Scanner;

public class pattern09 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            // space
            for (int j = i; j < n; j++) {
                System.out.print(" ");
            }

            // star
            for (int j = 1; j < i * 2; j++) {
                System.out.print("*");
            }

            System.out.println();
        }

        for (int i = n; i > 0; i--) {
            // space
            for (int j = i; j < n; j++) {
                System.out.print(" ");
            }

            // star
            for (int j = 1; j < i * 2; j++) {
                System.out.print("*");
            }

            System.out.println();
        }
    }
}
```

---

## pattern 10

![](./img/pattern%2010.png)

> `plane`

- formula calculate star and space then implement.

| star | space |
| ---- | ----- |
| 1    | 4     |
| 2    | 3     |
| 3    | 2     |
| 4    | 1     |
| 5    | 0     |
| 4    | 1     |
| 3    | 2     |
| 2    | 3     |
| 1    | 4     |

> `code`

```java
import java.util.Scanner;

public class pattern10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter N value: ");
        int n = sc.nextInt();

        for (int i = 1; i < n * 2; i++) {
            // calculation
            int star = i > n ? 2 * n - i : i;
            for (int j = 1; j <= star; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
```

---

## pattern 11

![](./img/pattern%2011.png)

> `plan`

even odd condition for print number.

> `code`

```java
import java.util.Scanner;

public class pattern11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        // first way
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                int number = (i + j) % 2 == 0 ? 1 : 0;
                System.out.print(number);
            }
            System.out.println();
        }

        // second way
        int number = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print(number);
                number = 1 - number;
            }
            System.out.println();
        }
    }
}
```

---

## pattern 12

![](./img/pattern%2012.png)

> `plan`

- number space(calculation) number

impotent use i = 1

| num | space | num |
| --- | ----- | --- |
| 1   | 6     | 1   |
| 2   | 4     | 2   |
| 3   | 2     | 3   |
| 4   | 0     | 4   |

> `code`

```java
import java.util.Scanner;

public class pattern12 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            // number
            for (int j = 1; j <= i; j++) {
                System.out.print(j);
            }

            // space
            int space = 2 * (n - i);
            for (int j = 1; j <= space; j++) {
                System.out.print("-");
            }

            // number
            for (int j = i; j >= 1; j--) {
                System.out.print(j);
            }
            System.out.println();
        }
    }
}
```

---

## pattern 13

![](./img/pattern%2013.png)

> `plan`

no plan for this.

> `code`

```java
import java.util.Scanner;

public class pattern13 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter N value: ");
        int n = sc.nextInt();

        int number = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print(number);
                System.out.print(" ");
                number++;
            }
            System.out.println();
        }
    }
}
```

---

## pattern 14

![](./img/pattern%2014.png)

> `plan`

no need.

> `code`

```java
import java.util.Scanner;

public class pattern14 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            for (char j = 'A'; j <= 'A' + i; j++) {
                System.out.print(j);
            }
            System.out.println();
        }
    }
}
```

---

## pattern 15

![](./img/pattern%2015.png)

> `plan`

no need.

> `code`

```java
import java.util.Scanner;

public class pattern15 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            for (char j = 'A'; j < 'A' + n - i; j++) {
                System.out.print(j);
            }
            System.out.println();
        }
    }
}
```

---

## patter 16

![](./img/pattern%2016.png)

> `plan`

no need

> `code`

```java
import java.util.Scanner;

public class pattern16 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            char ch = (char) ('A' + i);

            for (int j = 0; j <= i; j++) {
                System.out.print(ch);
            }
            System.out.println();
        }
    }
}
```

---

## patter 17

![](./img/pattern%2017.png)

> `plan`

space character

| space | character |
| ----- | --------- |
| 3     | 1         |
| 2     | 3         |
| 1     | 5         |
| 0     | 7         |

> `code`

```java
import java.util.Scanner;

public class pattern17 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            // space
            for (int j = n; j > i; j--) {
                System.out.print(" ");
            }

            // charter
            char ch = 'A';
            for (int j = 1; j < i * 2; j++) {
                System.out.print(ch);
                if (i > j) {
                    ch++;
                } else {
                    ch--;
                }
            }
            System.out.println();
        }
    }
}
```

---

## patter 18

![](./img/pattern%2018.png)

> `plan`

outer loop reverse, and then add inside ch.

> `code`

```java
import java.util.Scanner;

public class pattern18 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for (int i = n; i > 0; i--) {
            char ch = (char) ('A' + i - 1);
            for(int j = 0; j <= n - i; j++ ){
                System.out.print(ch);
                ch++;
            }
            System.out.println();
        }
    }
}
```

---

## patter 19

![](./img/pattern%2019.png)

> `plan`

star space star

| star | space | star |
| ---- | ----- | ---- |
| 5    | 0     | 5    |
| 4    | 2     | 4    |
| 3    | 4     | 3    |
| 2    | 6     | 2    |
| 1    | 8     | 1    |
| 1    | 8     | 1    |
| 2    | 6     | 2    |
| 3    | 4     | 3    |
| 4    | 2     | 4    |
| 5    | 0     | 5    |

---

## patter 20

![](./img/pattern%2020.png)

> `plan`

> `code`

```java
import java.util.Scanner;

public class pattern20 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            // star
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }

            // space
            int space = (n - i) * 2;
            for (int j = 0; j < space; j++) {
                System.out.print(" ");
            }

            // star
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        for (int i = n; i >= 1; i--) {
            // star
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }

            // space
            int space = (n - i) * 2;
            for (int j = 0; j < space; j++) {
                System.out.print(" ");
            }

            // star
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
```

---

## patter 21

![](./img/pattern%2021.png)

> `code`

```java
import java.util.Scanner;

public class pattern21 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == 1 || j == 1 || i == n || j == n) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}
```

---

## patter 22

![](./img/pattern%2022.png)

> `code`

```java
import java.util.Scanner;

public class pattern22 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for (int i = 1; i < n * 2; i++) {
            for (int j = 1; j < n * 2; j++) {
                int top = j - 1;
                int left = i - 1;
                int bottom = (n * 2) - j - 1;
                int right = (n * 2) - i - 1;

                int min = Math.min(Math.min(top, bottom), Math.min(left, right));
                System.out.print(n - min);
            }
            System.out.println();
        }
    }
}
```

---
