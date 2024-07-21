package de.lampe2020.textruct;

// External imports:
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Main {
    private static final Logger logger = LogManager.getLogger(Main.class);
    public static void main(String[] args) {
        logger.info("Hello world!");    /* I'll leave this here for now, as a little easteregg for people reading the
                                           code or the logs. */
        System.out.println(new InternalResource("assets/text/welcomeMessage.txt").string());
        //TODO: Implement argument handling with picocli and launching the actual game with the correct arguments
    }
}
