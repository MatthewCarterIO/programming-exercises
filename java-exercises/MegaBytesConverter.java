// Challenge summary: Convert an input of kilobytes to an output of megabytes and kilobytes.

public class MegaBytesConverter {

    public static void main(String[] args) {
        printMegaBytesAndKiloBytes(2050); // 2MB 2KB
        printMegaBytesAndKiloBytes(2048); // 2MB 0KB
        printMegaBytesAndKiloBytes(2046); // 1MB 1022KB
        printMegaBytesAndKiloBytes(3072); // 3MB 0KB
        printMegaBytesAndKiloBytes(-200); // Invalid
    }

    private static void printMegaBytesAndKiloBytes(int kiloBytes) {
        if (kiloBytes < 0) {
            System.out.println("Invalid Value");
        } else {
            // 1MB = 1024KB
            int megaBytes = kiloBytes / 1024;
            int remainingKiloBytes = kiloBytes % 1024;
            String output = kiloBytes + " KB = " + megaBytes + " MB and " + remainingKiloBytes + " KB";
            System.out.println(output);
        }
    }

}
