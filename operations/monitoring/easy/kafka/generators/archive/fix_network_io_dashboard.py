#!/usr/bin/env python3
"""
修复网络IO指标的Dashboard
使用可用的进程级网络指标替代系统级指标
"""

import json

def fix_network_io_panels():
    """修复网络IO面板，使用实际可用的指标"""
    
    # 修复后的网络IO面板
    network_io_panel = {
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
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 16},
        "id": 12,
        "options": {
            "legend": {"calcs": [], "displayMode": "list", "placement": "bottom", "showLegend": True},
            "tooltip": {"mode": "single", "sort": "none"}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "rate(process_network_receive_bytes_total[5m])",
                "legendFormat": "{{job}} 接收",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "rate(process_network_transmit_bytes_total[5m])",
                "legendFormat": "{{job}} 发送",
                "refId": "B"
            }
        ],
        "title": "进程网络IO速率",
        "type": "timeseries"
    }
    
    # Docker容器网络统计面板
    docker_network_panel = {
        "datasource": {"type": "prometheus", "uid": "prometheus"},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "custom": {
                    "align": "auto",
                    "cellOptions": {"type": "auto"},
                    "inspect": False
                },
                "mappings": [],
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "red", "value": 80}
                    ]
                }
            },
            "overrides": [
                {
                    "matcher": {"id": "byName", "options": "接收字节"},
                    "properties": [
                        {"id": "unit", "value": "decbytes"},
                        {"id": "custom.cellOptions", "value": {"type": "color-background"}}
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "发送字节"},
                    "properties": [
                        {"id": "unit", "value": "decbytes"},
                        {"id": "custom.cellOptions", "value": {"type": "color-background"}}
                    ]
                }
            ]
        },
        "gridPos": {"h": 8, "w": 24, "x": 0, "y": 24},
        "id": 13,
        "options": {
            "cellHeight": "sm",
            "footer": {"countRows": False, "fields": "", "reducer": ["sum"], "show": False},
            "showHeader": True
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "process_network_receive_bytes_total",
                "format": "table",
                "instant": True,
                "legendFormat": "__auto",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "process_network_transmit_bytes_total",
                "format": "table",
                "instant": True,
                "legendFormat": "__auto",
                "refId": "B"
            }
        ],
        "title": "进程网络统计表",
        "transformations": [
            {"id": "merge", "options": {}},
            {
                "id": "organize",
                "options": {
                    "excludeByName": {"Time": True, "__name__": True},
                    "renameByName": {
                        "job": "服务",
                        "instance": "实例",
                        "Value #A": "接收字节",
                        "Value #B": "发送字节"
                    }
                }
            }
        ],
        "type": "table"
    }
    
    return network_io_panel, docker_network_panel

def create_alternative_network_panels():
    """创建替代的网络监控面板"""
    
    # Kafka连接数面板 (使用JMX指标，如果可用)
    kafka_connections_panel = {
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
                "unit": "short"
            }
        },
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 32},
        "id": 14,
        "options": {
            "legend": {"calcs": [], "displayMode": "list", "placement": "bottom", "showLegend": True},
            "tooltip": {"mode": "single", "sort": "none"}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "kafka_server_socket_server_metrics_connection_count",
                "legendFormat": "Kafka连接数",
                "refId": "A"
            }
        ],
        "title": "Kafka连接数 (如果JMX可用)",
        "type": "timeseries"
    }
    
    # 进程资源使用面板
    process_resources_panel = {
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
                "unit": "short"
            }
        },
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 32},
        "id": 15,
        "options": {
            "legend": {"calcs": [], "displayMode": "list", "placement": "bottom", "showLegend": True},
            "tooltip": {"mode": "single", "sort": "none"}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "process_open_fds",
                "legendFormat": "{{job}} 打开文件数",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "process_resident_memory_bytes",
                "legendFormat": "{{job}} 内存使用",
                "refId": "B"
            }
        ],
        "title": "进程资源使用",
        "type": "timeseries"
    }
    
    return kafka_connections_panel, process_resources_panel

if __name__ == "__main__":
    print("✅ 网络IO修复面板创建完成")
    print("📊 可用指标:")
    print("   • process_network_receive_bytes_total")
    print("   • process_network_transmit_bytes_total")
    print("   • process_open_fds")
    print("   • process_resident_memory_bytes")
