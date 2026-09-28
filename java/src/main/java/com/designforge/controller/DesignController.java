package com.designforge.controller;

import com.designforge.model.DesignTask;
import com.designforge.service.DesignService;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/design")
public class DesignController {

    private final DesignService designService;

    public DesignController(DesignService designService) {
        this.designService = designService;
    }

    @GetMapping
    public List<DesignTask> getAllTasks() {
        return designService.getAllTasks();
    }

    @PostMapping
    public ResponseEntity<DesignTask> createTask(@Valid @RequestBody DesignTask task) {
        return ResponseEntity.ok(designService.createTask(task));
    }

    @GetMapping("/{id}")
    public ResponseEntity<DesignTask> getTask(@PathVariable String id) {
        return ResponseEntity.of(designService.getTask(id));
    }
}
