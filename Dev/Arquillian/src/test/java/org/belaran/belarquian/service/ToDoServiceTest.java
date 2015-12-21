package org.belaran.belarquian.service;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;

import org.jboss.arquillian.container.test.api.Deployment;
import org.jboss.arquillian.container.test.api.RunAsClient;
import org.jboss.arquillian.junit.Arquillian;
import org.jboss.arquillian.junit.InSequence;
import org.jboss.arquillian.test.api.ArquillianResource;
import org.jboss.shrinkwrap.api.ShrinkWrap;
import org.jboss.shrinkwrap.api.importer.ZipImporter;
import org.jboss.shrinkwrap.api.spec.WebArchive;
import org.junit.Test;
import org.junit.runner.RunWith;

@RunWith(Arquillian.class)
public class ToDoServiceTest {

	private static final String ARTEFACT_NAME = "Belarquian.war";
	private static final String TARGET_DIR = "target";

	@ArquillianResource
	private URL baseURL;

	@Deployment
	public static WebArchive createDeployment() {
		return ShrinkWrap.create(ZipImporter.class, ARTEFACT_NAME)
				.importFrom(new File(TARGET_DIR + "/" + ARTEFACT_NAME))
				.as(WebArchive.class);
	}

	@Test
	@RunAsClient
	@InSequence(1)
	public void checkServiceStatus()
			throws IOException {
		printInputStream(baseURL.toString() + "rest/test");
	}

	@Test
	@RunAsClient
	@InSequence(2)
	public void addOneItemTest()
			throws IOException {
		printInputStream(baseURL.toString() + "rest/add/1/a-value");
	}

	@Test
	@RunAsClient
	@InSequence(3)
	public void listItems()
			throws IOException {
		printInputStream(baseURL.toString() + "rest/list");
	}

	private static void printInputStream(String urlAsString) throws IOException {
		System.out.println("Invoking URL:" + urlAsString);
		BufferedReader in = new BufferedReader(new InputStreamReader(new URL(urlAsString).openStream()));
		String inputLine;
		while ((inputLine = in.readLine()) != null)
		    System.out.println(inputLine);
		in.close();
	}

}
