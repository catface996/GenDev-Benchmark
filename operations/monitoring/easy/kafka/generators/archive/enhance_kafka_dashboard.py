#!/usr/bin/env python3
"""
增强Kafka Dashboard，添加CPU、内存、磁盘、连接数等系统级指标
"""

import json

def create_enhanced_kafka_dashboard():
    """创建增强版的Kafka Dashboard"""
    
    # 基础Dashboard结构
    dashboard = {
        "annotations": {
            "list": [
                {
                    "builtIn": 1,
                    "datasource": {"type": "grafana", "uid": "-- Grafana --"},
                    "enable": True,
                    "hide": True,
                    "iconColor": "rgba(0, 211, 255, 1)",
                    "name": "Annotations & Alerts",
                    "type": "dashboard"
                }
            ]
        },
        "editable": True,
        "fiscalYearStartMonth": 0,
        "graphTooltip": 0,
        "id": None,
        "links": [],
        "liveNow": False,
        "panels": [],
        "refresh": "30s",
        "schemaVersion": 38,
        "style": "dark",
        "tags": ["kafka", "monitoring", "system", "performance"],
        "templating": {"list": []},
        "time": {"from": "now-1h", "to": "now"},
        "timepicker": {},
        "timezone": "",
        "title": "Kafka增强监控Dashboard - 系统级指标",
        "uid": "kafka-enhanced-system-dashboard",
        "version": 1,
        "weekStart": ""
    }
    
    panels = []
    panel_id = 1
    
    # 第一行：系统资源统计 (6个stat面板)
    y_pos = 0
    
    # CPU使用率
    panels.append({
        "datasource": {"type": "prometheus", "uid": "prometheus"},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "mappings": [],
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "yellow", "value": 70},
                        {"color": "red", "value": 90}
                    ]
                },
                "unit": "percent"
            }
        },
        "gridPos": {"h": 4, "w": 4, "x": 0, "y": y_pos},
        "id": panel_id,
        "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "textMode": "auto"
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "100 - (avg(irate(node_cpu_seconds_total{mode=\"idle\"}[5m])) * 100)",
                "legendFormat": "CPU使用率",
                "refId": "A"
            }
        ],
        "title": "CPU使用率",
        "type": "stat"
    })
    panel_id += 1
    
    # 内存使用率
    panels.append({
        "datasource": {"type": "prometheus", "uid": "prometheus"},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "mappings": [],
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "yellow", "value": 80},
                        {"color": "red", "value": 95}
                    ]
                },
                "unit": "percent"
            }
        },
        "gridPos": {"h": 4, "w": 4, "x": 4, "y": y_pos},
        "id": panel_id,
        "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "textMode": "auto"
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100",
                "legendFormat": "内存使用率",
                "refId": "A"
            }
        ],
        "title": "内存使用率",
        "type": "stat"
    })
    panel_id += 1
    
    # 磁盘使用率
    panels.append({
        "datasource": {"type": "prometheus", "uid": "prometheus"},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "mappings": [],
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "yellow", "value": 80},
                        {"color": "red", "value": 95}
                    ]
                },
                "unit": "percent"
            }
        },
        "gridPos": {"h": 4, "w": 4, "x": 8, "y": y_pos},
        "id": panel_id,
        "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "textMode": "auto"
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "(1 - (node_filesystem_avail_bytes{fstype!=\"tmpfs\"} / node_filesystem_size_bytes{fstype!=\"tmpfs\"})) * 100",
                "legendFormat": "磁盘使用率",
                "refId": "A"
            }
        ],
        "title": "磁盘使用率",
        "type": "stat"
    })
    panel_id += 1
    
    # 网络连接数
    panels.append({
        "datasource": {"type": "prometheus", "uid": "prometheus"},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "mappings": [],
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "yellow", "value": 1000},
                        {"color": "red", "value": 5000}
                    ]
                },
                "unit": "short"
            }
        },
        "gridPos": {"h": 4, "w": 4, "x": 12, "y": y_pos},
        "id": panel_id,
        "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "textMode": "auto"
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "node_netstat_Tcp_CurrEstab",
                "legendFormat": "TCP连接数",
                "refId": "A"
            }
        ],
        "title": "TCP连接数",
        "type": "stat"
    })
    panel_id += 1
    
    # JVM堆内存使用
    panels.append({
        "datasource": {"type": "prometheus", "uid": "prometheus"},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "mappings": [],
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "yellow", "value": 70},
                        {"color": "red", "value": 90}
                    ]
                },
                "unit": "percent"
            }
        },
        "gridPos": {"h": 4, "w": 4, "x": 16, "y": y_pos},
        "id": panel_id,
        "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "textMode": "auto"
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "(jvm_memory_heap_used_bytes / jvm_memory_heap_max_bytes) * 100",
                "legendFormat": "JVM堆内存使用率",
                "refId": "A"
            }
        ],
        "title": "JVM堆内存使用率",
        "type": "stat"
    })
    panel_id += 1
    
    # 文件描述符使用率
    panels.append({
        "datasource": {"type": "prometheus", "uid": "prometheus"},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "mappings": [],
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "yellow", "value": 80},
                        {"color": "red", "value": 95}
                    ]
                },
                "unit": "percent"
            }
        },
        "gridPos": {"h": 4, "w": 4, "x": 20, "y": y_pos},
        "id": panel_id,
        "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "textMode": "auto"
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "(node_filefd_allocated / node_filefd_maximum) * 100",
                "legendFormat": "文件描述符使用率",
                "refId": "A"
            }
        ],
        "title": "文件描述符使用率",
        "type": "stat"
    })
    panel_id += 1
    
    return dashboard, panels, panel_id

if __name__ == "__main__":
    dashboard, panels, panel_id = create_enhanced_kafka_dashboard()
    print(f"✅ 基础Dashboard结构创建完成，包含 {len(panels)} 个面板")
    print("📊 已添加系统资源统计面板")
