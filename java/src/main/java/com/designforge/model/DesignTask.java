package com.designforge.model;

import jakarta.validation.constraints.NotBlank;

public record DesignTask(
        @NotBlank String id,
        @NotBlank String projectName,
        @NotBlank String designType,
        String status,
        String owner,
        String exportFormat
) {
}
