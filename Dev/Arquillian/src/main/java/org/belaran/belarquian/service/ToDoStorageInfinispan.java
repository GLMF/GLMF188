package org.belaran.belarquian.service;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import javax.annotation.PostConstruct;
import javax.cache.Cache;
import javax.cache.Cache.Entry;
import javax.cache.Caching;
import javax.cache.configuration.MutableConfiguration;
import javax.enterprise.context.ApplicationScoped;
import javax.enterprise.inject.Default;
import javax.inject.Named;

@Default
@Named
@ApplicationScoped
public class ToDoStorageInfinispan {

	private static final String CACHE_NAME = ToDoStorageInfinispan.class
			.getName();

	private Cache<Long, String> storage;

	@PostConstruct
	public void loadCache() {
		storage = Caching
				.getCachingProvider()
				.getCacheManager()
				.createCache(CACHE_NAME,
						new MutableConfiguration<Long, String>());
		if (storage == null)
			throw new IllegalStateException("Can't retrieve storage for "
					+ CACHE_NAME + " in cache manager.");
	}

	public List<ToDoItem> retrieve() {
		List<ToDoItem> items = new ArrayList<>();
		Iterator<Entry<Long, String>> iterator = storage.iterator();
		while (iterator.hasNext()) {
			Entry<Long, String> entry = iterator.next();
			items.add(new ToDoItem(entry.getKey(), entry.getValue()));
		}
		return items;
	}

	public void synchronize(List<ToDoItem> items) {
		for (ToDoItem item : items)
			storage.put(item.id, item.label);
	}
}
