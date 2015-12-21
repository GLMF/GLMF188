package org.belaran.belarquian.service;

public class ToDoItem {
	public long id;
	public String label;

	public ToDoItem(long id, String label) {
		this.id = id;
		this.label = label;
	}

	@Override
	public String toString() {
		return "(" + id + ") " + label;
	}
	
	
}