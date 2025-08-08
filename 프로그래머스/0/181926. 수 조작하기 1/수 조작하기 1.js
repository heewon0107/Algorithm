function solution(n, control) {
    for (i=0; i < control.length; i++) {
        const val = control.charAt(i);
        switch (val) {
            case "w":
                n++;
                break;
            case "s":
                n--;
                break;
            case "d":
                n += 10;
                break;
            case "a":
                n -= 10;
                break;
        }
    }
    return n;
}