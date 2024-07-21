package de.lampe2020.textruct;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class InternalResource {
    private final Logger logger = LogManager.getLogger(InternalResource.class);

    private String path;

    public InternalResource(String path) {
        this.path = path;
        logger.trace("Setting path for new InternalResource to {}", path);
    }

    public InputStream stream() {
        logger.trace("Reading internal resource {} as stream", this.path);
        return this.getClass().getClassLoader().getResourceAsStream(this.path);
    }

    public String string() {
        return string(StandardCharsets.UTF_8);
    }
    public String string(Charset charset) {
        logger.trace("Reading internal resource {} as {}-encoded string", this.path, charset);
        return new Scanner(this.stream(), charset).useDelimiter("\\A").next();
    }
}
