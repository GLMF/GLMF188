package org.belaran.belarquian.service;

import javax.inject.Inject;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.Response;

@Path("/")
public class ToDoServiceRS {

	@Inject
	private TodoService todoService;

	private final static String EOL = "\n";
	
	@GET
	@Path("/test")
	@Produces("text/plain")
	// curl http://127.0.0.1:8080/SimpleWebServiceReST/rest/test
	public Response test() {
		return Response.ok(this.getClass() + " service is up and running.\n").build();
	}

	@GET
	@Path("/list")
	@Produces("text/plain")
	public Response list() {
		System.out.println("list() has been invoked !");
		StringBuffer result = new StringBuffer();
		for ( ToDoItem item : todoService.getTodos() ) {
			result = result.append(item.toString()).append(EOL);
		}
		System.out.println("call to ToDoService finished with result:" + result);
		return Response.ok(result.append(EOL)).build();
	}
	
	@GET // should be a PUT !
	@Path("/add/{id}/{value}")
	@Produces("text/plain")
	public Response add(@PathParam(value="id") long id, @PathParam(value="value")  String param) {
		System.out.println("add() has been invoked with param:" + param);
		todoService.addToDo(new ToDoItem(id, param));
		return Response.ok("Item:" + id + "," + param + " - added.").build();
	}
	
}
