#!/usr/bin/env python3
"""
添加系统级监控面板到Kafka Dashboard
"""

def add_system_monitoring_panels(panels, panel_id, y_pos):
    """添加系统监控面板"""
    
    # 第二行：CPU和内存详细监控 (2个时间序列面板)
    y_pos += 4
    
    # CPU详细监控
    panels.append({
        "datasource": {"type": "prometheus", "uid": "prometheus"},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "custom": {
                    "axisCenteredZero": False,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 10,
                    "gradientMode": "none",
                    "hideFrom": {"legend": False, "tooltip": False, "vis": False},
                    "insertNulls": False,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {"type": "linear"},
                    "showPoints": "never",
                    "spanNulls": False,
                    "stacking": {"group": "A", "mode": "percent"},
                    "thresholdsStyle": {"mode": "off"}
                },
                "mappings": [],
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "red", "value": 80}
                    ]
                },
                "unit": "percent"
            }
        },
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": y_pos},
        "id": panel_id,
        "options": {
            "legend": {"calcs": [], "displayMode": "list", "placement": "bottom", "showLegend": True},
            "tooltip": {"mode": "single", "sort": "none"}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "100 - (avg(irate(node_cpu_seconds_total{mode=\"idle\"}[5m])) * 100)",
                "legendFormat": "CPU使用率",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "avg(irate(node_cpu_seconds_total{mode=\"system\"}[5m])) * 100",
                "legendFormat": "系统CPU",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "avg(irate(node_cpu_seconds_total{mode=\"user\"}[5m])) * 100",
                "legendFormat": "用户CPU",
                "refId": "C"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "avg(irate(node_cpu_seconds_total{mode=\"iowait\"}[5m])) * 100",
                "legendFormat": "IO等待",
                "refId": "D"
            }
        ],
        "title": "CPU使用详情",
        "type": "timeseries"
    })
    panel_id += 1
    
    # 内存详细监控
    panels.append({
        "datasource": {"type": "prometheus", "uid": "prometheus"},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "custom": {
                    "axisCenteredZero": False,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 10,
                    "gradientMode": "none",
                    "hideFrom": {"legend": False, "tooltip": False, "vis": False},
                    "insertNulls": False,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {"type": "linear"},
                    "showPoints": "never",
                    "spanNulls": False,
                    "stacking": {"group": "A", "mode": "none"},
                    "thresholdsStyle": {"mode": "off"}
                },
                "mappings": [],
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "red", "value": 80}
                    ]
                },
                "unit": "decbytes"
            }
        },
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": y_pos},
        "id": panel_id,
        "options": {
            "legend": {"calcs": [], "displayMode": "list", "placement": "bottom", "showLegend": True},
            "tooltip": {"mode": "single", "sort": "none"}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "node_memory_MemTotal_bytes",
                "legendFormat": "总内存",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes",
                "legendFormat": "已用内存",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "node_memory_MemAvailable_bytes",
                "legendFormat": "可用内存",
                "refId": "C"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "node_memory_Cached_bytes",
                "legendFormat": "缓存",
                "refId": "D"
            }
        ],
        "title": "内存使用详情",
        "type": "timeseries"
    })
    panel_id += 1
    
    # 第三行：磁盘和网络监控 (2个时间序列面板)
    y_pos += 8
    
    # 磁盘IO监控
    panels.append({
        "datasource": {"type": "prometheus", "uid": "prometheus"},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "custom": {
                    "axisCenteredZero": False,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 10,
                    "gradientMode": "none",
                    "hideFrom": {"legend": False, "tooltip": False, "vis": False},
                    "insertNulls": False,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {"type": "linear"},
                    "showPoints": "never",
                    "spanNulls": False,
                    "stacking": {"group": "A", "mode": "none"},
                    "thresholdsStyle": {"mode": "off"}
                },
                "mappings": [],
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "red", "value": 80}
                    ]
                },
                "unit": "binBps"
            }
        },
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": y_pos},
        "id": panel_id,
        "options": {
            "legend": {"calcs": [], "displayMode": "list", "placement": "bottom", "showLegend": True},
            "tooltip": {"mode": "single", "sort": "none"}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "rate(node_disk_read_bytes_total[5m])",
                "legendFormat": "磁盘读取 - {{device}}",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "rate(node_disk_written_bytes_total[5m])",
                "legendFormat": "磁盘写入 - {{device}}",
                "refId": "B"
            }
        ],
        "title": "磁盘IO速率",
        "type": "timeseries"
    })
    panel_id += 1
    
    # 网络IO监控
    panels.append({
        "datasource": {"type": "prometheus", "uid": "prometheus"},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "custom": {
                    "axisCenteredZero": False,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 10,
                    "gradientMode": "none",
                    "hideFrom": {"legend": False, "tooltip": False, "vis": False},
                    "insertNulls": False,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {"type": "linear"},
                    "showPoints": "never",
                    "spanNulls": False,
                    "stacking": {"group": "A", "mode": "none"},
                    "thresholdsStyle": {"mode": "off"}
                },
                "mappings": [],
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "red", "value": 80}
                    ]
                },
                "unit": "binBps"
            }
        },
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": y_pos},
        "id": panel_id,
        "options": {
            "legend": {"calcs": [], "displayMode": "list", "placement": "bottom", "showLegend": True},
            "tooltip": {"mode": "single", "sort": "none"}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "rate(node_network_receive_bytes_total{device!=\"lo\"}[5m])",
                "legendFormat": "网络接收 - {{device}}",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "rate(node_network_transmit_bytes_total{device!=\"lo\"}[5m])",
                "legendFormat": "网络发送 - {{device}}",
                "refId": "B"
            }
        ],
        "title": "网络IO速率",
        "type": "timeseries"
    })
    panel_id += 1
    
    return panels, panel_id, y_pos

def add_jvm_monitoring_panels(panels, panel_id, y_pos):
    """添加JVM监控面板"""
    
    # 第四行：JVM详细监控 (2个时间序列面板)
    y_pos += 8
    
    # JVM内存详细监控
    panels.append({
        "datasource": {"type": "prometheus", "uid": "prometheus"},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "custom": {
                    "axisCenteredZero": False,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 10,
                    "gradientMode": "none",
                    "hideFrom": {"legend": False, "tooltip": False, "vis": False},
                    "insertNulls": False,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {"type": "linear"},
                    "showPoints": "never",
                    "spanNulls": False,
                    "stacking": {"group": "A", "mode": "none"},
                    "thresholdsStyle": {"mode": "off"}
                },
                "mappings": [],
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "red", "value": 80}
                    ]
                },
                "unit": "decbytes"
            }
        },
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": y_pos},
        "id": panel_id,
        "options": {
            "legend": {"calcs": [], "displayMode": "list", "placement": "bottom", "showLegend": True},
            "tooltip": {"mode": "single", "sort": "none"}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "jvm_memory_heap_used_bytes",
                "legendFormat": "堆内存使用",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "jvm_memory_heap_max_bytes",
                "legendFormat": "堆内存最大",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "jvm_memory_nonheap_used_bytes",
                "legendFormat": "非堆内存使用",
                "refId": "C"
            }
        ],
        "title": "JVM内存使用详情",
        "type": "timeseries"
    })
    panel_id += 1
    
    # JVM垃圾回收监控
    panels.append({
        "datasource": {"type": "prometheus", "uid": "prometheus"},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "custom": {
                    "axisCenteredZero": False,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 10,
                    "gradientMode": "none",
                    "hideFrom": {"legend": False, "tooltip": False, "vis": False},
                    "insertNulls": False,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {"type": "linear"},
                    "showPoints": "never",
                    "spanNulls": False,
                    "stacking": {"group": "A", "mode": "none"},
                    "thresholdsStyle": {"mode": "off"}
                },
                "mappings": [],
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "red", "value": 80}
                    ]
                },
                "unit": "ms"
            }
        },
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": y_pos},
        "id": panel_id,
        "options": {
            "legend": {"calcs": [], "displayMode": "list", "placement": "bottom", "showLegend": True},
            "tooltip": {"mode": "single", "sort": "none"}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "rate(jvm_gc_collection_time_ms_total[5m])",
                "legendFormat": "GC时间 - {{gc}}",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "rate(jvm_gc_collection_count_total[5m])",
                "legendFormat": "GC次数 - {{gc}}",
                "refId": "B"
            }
        ],
        "title": "JVM垃圾回收",
        "type": "timeseries"
    })
    panel_id += 1
    
    return panels, panel_id, y_pos

if __name__ == "__main__":
    print("✅ 系统监控面板函数创建完成")
