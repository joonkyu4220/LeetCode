int rev = 0;
        // 2147483648;
        while (x)
        {
            if ((rev > 214748364) || (rev < -214748364))
                return 0;
            rev = 10 * rev + x % 10;
            x /= 10;
        }
        return rev;
