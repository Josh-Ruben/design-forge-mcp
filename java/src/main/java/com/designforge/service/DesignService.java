package com.designforge.service;

import com.designforge.model.DesignTask;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;

@Service
public class DesignService {
    private final Map<String, DesignTask> tasks = new ConcurrentHashMap<>();

    public List<DesignTask> getAllTasks() {
        return new ArrayList<>(tasks.values());
    }

    public DesignTask createTask(DesignTask task) {
        tasks.put(task.id(), task);
        return task;
    }

    public Optional<DesignTask> getTask(String id) {
        return Optional.ofNullable(tasks.get(id));
    }
}
