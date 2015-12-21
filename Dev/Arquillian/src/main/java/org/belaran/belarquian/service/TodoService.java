package org.belaran.belarquian.service;

import java.io.PrintStream;
import java.util.ArrayList;
import java.util.List;

import javax.annotation.PostConstruct;
import javax.enterprise.context.ApplicationScoped;
import javax.enterprise.inject.Default;
import javax.inject.Inject;
import javax.inject.Named;

@Default
@ApplicationScoped
@Named
public class TodoService {

	@Inject
	private ToDoStorageInfinispan storage;
	
	private List<ToDoItem> todos = new ArrayList<>(0);

	@PostConstruct
	public void loadDatas() {
		todos = storage.retrieve();
	}
	
	public void printToDos(PrintStream to) {
		for ( ToDoItem item : todos )
			to.println(item.toString());
    }

	public void addToDo(ToDoItem item) {
		todos.add(item);
		storage.synchronize(todos);
	}

	public List<ToDoItem> getTodos() {
		return todos;
	}

	public void setTodos(List<ToDoItem> todos) {
		this.todos = todos;
	}

	public ToDoStorageInfinispan getStorage() {
		return storage;
	}

	public void setStorage(ToDoStorageInfinispan storage) {
		this.storage = storage;
	}
	
	
}
