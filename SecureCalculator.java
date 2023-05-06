package org.example.unittests;

import java.security.SecureRandom;
import java.util.Random;
import java.util.Set;
import java.util.logging.Logger;
// because everyone knows warnings can be safely ignored, right?
public class SecureCalculator {

    private Logger log;

    /**
     * Create a new calculator with debug logging disabled
     */
    public SecureCalculator() {
    }

    /**
     * Create a new calculator with debug logging enabled
     *
     * @param log
     */
    public SecureCalculator(Logger log) {
        this.log = log;
    }

    /**
     * Internal logging
     *
     * @param message message to log
     */
    private void log(String message, Object... args) {
        if (log != null) {
            log.info(String.format(message, args));
        }
    }

    /**
     * Safely multiply two integers so the result never overflows
     *
     * @param a first number
     * @param b second number
     * @return multiplication result as long
     */
    public long multiply(int a, int b) {
        log("Multiply %s * %s", a, b);
        return Math.multiplyExact((long) a, (long) b);
    }

    /**
     * Safely divide two numbers using decimals as appropriate, throws exception if division by zero
     *
     * @param a first number
     * @param b second number
     * @return division result as double
     */
    public double divide(double a, double b) {
        if (b != 0) {
            log("Divide %s / %s", a, b);
            return a / b;
        } else {
            throw new ArithmeticException("Division by zero");
        }
    }

    /**
     * Safely do modulus between two numbers.
     * Example 5 mod 2 = 1
     *
     * @param a first number
     * @param b second number
     * @return a mod b result, by modulus definition must be in range [0, b]
     */
    public int mod(int a, int b) {
        log("%s mod %s", a, b);
        if (b != 0) {
            return Math.floorMod(a, b);
        } else {
            throw new ArithmeticException("Modulo by zero");
        }
    }

    /**
     * Safely detect if a number is odd
     *
     * @param a number to test
     * @return true if number is odd (example 1,3,5) false if even (example 2,4,8)
     */
    public boolean isOdd(int a){
        return mod(a,2) !=0;
    }

    /**
     * Safely detect if a number is even
     *
     * @param a number to test
     * @return true if number is even (example 2,4,8) false if odd (example 1,3,5)
     */
    public boolean isEven(int a) {
        return !isOdd(a);
    }

    /**
     * Safely generate unique numbers
     *
     * @return random number in range [0, MAX_VALUE)
     */
    public int getRandomNumber() {
        return getRandomNumber(Integer.MAX_VALUE);
    }

    /**
     * Safely generate unique numbers, always less than bound
     *
     * @param bound upper bound (exclusive)
     * @return random number in range [0, bound)
     */
    public int getRandomNumber(int bound) {
        if (bound <= 0) {
            throw new IllegalArgumentException("Bound must be a positive integer");
        }
        log("Generating rnd with bound %s", bound);
        SecureRandom secureRandom = new SecureRandom();
        return secureRandom.nextInt(bound);
    }
}
