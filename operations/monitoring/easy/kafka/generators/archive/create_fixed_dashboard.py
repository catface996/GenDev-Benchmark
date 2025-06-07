#!/usr/bin/env python3
"""
创建修复版的Kafka Dashboard，使用实际可用的网络指标
"""

import json

def create_fixed_kafka_dashboard():
    """创建修复版的Kafka Dashboard"""
    
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
        "tags": ["kafka", "monitoring", "fixed", "network-io"],
        "templating": {"list": []},
        "time": {"from": "now-1h", "to": "now"},
        "timepicker": {},
        "timezone": "",
        "title": "Kafka监控Dashboard - 修复版",
        "uid": "kafka-fixed-dashboard",
        "version": 1,
        "weekStart": ""
    }
    
    panels = []
    panel_id = 1
    
    # 第一行：基础统计 (4个stat面板)
    y_pos = 0
    
    # Topic总数
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
                        {"color": "red", "value": 80}
                    ]
                },
                "unit": "short"
            }
        },
        "gridPos": {"h": 4, "w": 6, "x": 0, "y": y_pos},
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
                "expr": "count by () (group by (topic) (kafka_topic_partitions{topic!~\"__.*\"}))",
                "legendFormat": "__auto",
                "refId": "A"
            }
        ],
        "title": "Topic总数",
        "type": "stat"
    })
    panel_id += 1
    
    # 总消息数
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
                        {"color": "red", "value": 80}
                    ]
                },
                "unit": "short"
            }
        },
        "gridPos": {"h": 4, "w": 6, "x": 6, "y": y_pos},
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
                "expr": "sum(kafka_topic_partition_current_offset{topic!~\"__.*\"})",
                "legendFormat": "__auto",
                "refId": "A"
            }
        ],
        "title": "总消息数",
        "type": "stat"
    })
    panel_id += 1
    
    # 消费者组数量
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
                        {"color": "yellow", "value": 5},
                        {"color": "red", "value": 20}
                    ]
                },
                "unit": "short"
            }
        },
        "gridPos": {"h": 4, "w": 6, "x": 12, "y": y_pos},
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
                "expr": "count by () (group by (consumer_group) (kafka_consumer_lag_messages))",
                "legendFormat": "__auto",
                "refId": "A"
            }
        ],
        "title": "消费者组数量",
        "type": "stat"
    })
    panel_id += 1
    
    # 总积压消息数
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
                        {"color": "yellow", "value": 100},
                        {"color": "red", "value": 1000}
                    ]
                },
                "unit": "short"
            }
        },
        "gridPos": {"h": 4, "w": 6, "x": 18, "y": y_pos},
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
                "expr": "sum(kafka_consumer_lag_messages)",
                "legendFormat": "__auto",
                "refId": "A"
            }
        ],
        "title": "总积压消息数",
        "type": "stat"
    })
    panel_id += 1
    
    # 第二行：Topic和Consumer监控 (2个时间序列面板)
    y_pos += 4
    
    # Topic消息生产速率
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
                "unit": "reqps"
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
                "expr": "sum by (topic) (rate(kafka_topic_partition_current_offset{topic!~\"__.*\"}[5m]))",
                "legendFormat": "{{topic}}",
                "refId": "A"
            }
        ],
        "title": "Topic消息生产速率",
        "type": "timeseries"
    })
    panel_id += 1
    
    # Consumer积压趋势
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
                "unit": "short"
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
                "expr": "sum by (consumer_group) (kafka_consumer_lag_messages)",
                "legendFormat": "{{consumer_group}}",
                "refId": "A"
            }
        ],
        "title": "Consumer积压趋势",
        "type": "timeseries"
    })
    panel_id += 1
    
    # 第三行：修复的网络IO监控 (2个面板)
    y_pos += 8
    
    # 进程网络IO速率 (使用实际可用的指标)
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
        "title": "进程网络IO速率 (修复版)",
        "type": "timeseries"
    })
    panel_id += 1
    
    # 进程资源使用
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
                "unit": "short"
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
                "expr": "process_open_fds",
                "legendFormat": "{{job}} 打开文件数",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "process_resident_memory_bytes / 1024 / 1024",
                "legendFormat": "{{job}} 内存使用(MB)",
                "refId": "B"
            }
        ],
        "title": "进程资源使用",
        "type": "timeseries"
    })
    panel_id += 1
    
    # 第四行：网络统计表格
    y_pos += 8
    
    # 进程网络统计表
    panels.append({
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
        "gridPos": {"h": 8, "w": 24, "x": 0, "y": y_pos},
        "id": panel_id,
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
        "title": "进程网络统计表 (实际数据)",
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
    })
    
    dashboard["panels"] = panels
    return dashboard

if __name__ == "__main__":
    dashboard = create_fixed_kafka_dashboard()
    
    # 保存到文件
    with open("kafka-dashboard-fixed.json", "w", encoding="utf-8") as f:
        json.dump(dashboard, f, indent=2, ensure_ascii=False)
    
    print("✅ 修复版Kafka Dashboard已生成: kafka-dashboard-fixed.json")
    print(f"📊 包含 {len(dashboard['panels'])} 个监控面板")
    print("🔧 修复内容:")
    print("   • 使用 process_network_receive_bytes_total 替代 node_network_*")
    print("   • 使用 process_network_transmit_bytes_total 替代系统级网络指标")
    print("   • 添加进程资源监控 (文件描述符、内存)")
    print("   • 添加网络统计表格显示实际数据")
    print("🚀 可直接导入到Grafana中使用")
