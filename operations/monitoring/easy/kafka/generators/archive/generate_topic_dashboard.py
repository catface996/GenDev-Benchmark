#!/usr/bin/env python3
"""
生成Kafka Topic维度监控Dashboard
包含Topic选择器和相关的所有监控面板
"""

import json

def create_topic_dashboard():
    """生成Topic维度的Dashboard配置"""
    
    # 基础Dashboard结构
    dashboard = {
        "annotations": {
            "list": [
                {
                    "builtIn": 1,
                    "datasource": {
                        "type": "grafana",
                        "uid": "-- Grafana --"
                    },
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
        "tags": ["kafka", "topic", "monitoring"],
        "templating": {
            "list": [
                {
                    "current": {
                        "selected": False,
                        "text": "All",
                        "value": "$__all"
                    },
                    "datasource": {
                        "type": "prometheus",
                        "uid": "prometheus"
                    },
                    "definition": "label_values(kafka_topic_partitions{topic!~\"__.*\"}, topic)",
                    "hide": 0,
                    "includeAll": True,
                    "label": "Topic",
                    "multi": False,
                    "name": "topic",
                    "options": [],
                    "query": {
                        "query": "label_values(kafka_topic_partitions{topic!~\"__.*\"}, topic)",
                        "refId": "StandardVariableQuery"
                    },
                    "refresh": 1,
                    "regex": "",
                    "skipUrlSync": False,
                    "sort": 1,
                    "type": "query"
                }
            ]
        },
        "time": {"from": "now-1h", "to": "now"},
        "timepicker": {},
        "timezone": "",
        "title": "Kafka Topic详细监控Dashboard",
        "uid": "kafka-topic-dashboard",
        "version": 1,
        "weekStart": ""
    }
    
    panels = []
    panel_id = 1
    
    # 第一行：Topic基础统计 (4个stat面板)
    y_pos = 0
    
    # Topic分区数
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
            },
            "overrides": []
        },
        "gridPos": {"h": 4, "w": 6, "x": 0, "y": y_pos},
        "id": panel_id,
        "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
                "calcs": ["lastNotNull"],
                "fields": "",
                "values": False
            },
            "textMode": "auto"
        },
        "pluginVersion": "10.0.0",
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "editorMode": "code",
                "expr": "kafka_topic_partitions{topic=~\"$topic\"}",
                "instant": False,
                "legendFormat": "__auto",
                "range": True,
                "refId": "A"
            }
        ],
        "title": "分区数",
        "type": "stat"
    })
    panel_id += 1
    
    # Topic消息总数
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
            },
            "overrides": []
        },
        "gridPos": {"h": 4, "w": 6, "x": 6, "y": y_pos},
        "id": panel_id,
        "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
                "calcs": ["lastNotNull"],
                "fields": "",
                "values": False
            },
            "textMode": "auto"
        },
        "pluginVersion": "10.0.0",
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "editorMode": "code",
                "expr": "sum(kafka_topic_partition_current_offset{topic=~\"$topic\"})",
                "instant": False,
                "legendFormat": "__auto",
                "range": True,
                "refId": "A"
            }
        ],
        "title": "消息总数",
        "type": "stat"
    })
    panel_id += 1
    
    # Topic生产速率
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
                "unit": "reqps"
            },
            "overrides": []
        },
        "gridPos": {"h": 4, "w": 6, "x": 12, "y": y_pos},
        "id": panel_id,
        "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
                "calcs": ["lastNotNull"],
                "fields": "",
                "values": False
            },
            "textMode": "auto"
        },
        "pluginVersion": "10.0.0",
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "editorMode": "code",
                "expr": "sum(rate(kafka_topic_partition_current_offset{topic=~\"$topic\"}[5m]))",
                "instant": False,
                "legendFormat": "__auto",
                "range": True,
                "refId": "A"
            }
        ],
        "title": "生产速率",
        "type": "stat"
    })
    panel_id += 1
    
    # Topic积压消息数
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
                        {"color": "yellow", "value": 10},
                        {"color": "red", "value": 100}
                    ]
                },
                "unit": "short"
            },
            "overrides": []
        },
        "gridPos": {"h": 4, "w": 6, "x": 18, "y": y_pos},
        "id": panel_id,
        "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
                "calcs": ["lastNotNull"],
                "fields": "",
                "values": False
            },
            "textMode": "auto"
        },
        "pluginVersion": "10.0.0",
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "editorMode": "code",
                "expr": "sum(kafka_consumer_lag_messages{topic=~\"$topic\"})",
                "instant": False,
                "legendFormat": "__auto",
                "range": True,
                "refId": "A"
            }
        ],
        "title": "积压消息数",
        "type": "stat"
    })
    panel_id += 1
    
    # 第二行：消息趋势和分区分布 (2个时间序列面板)
    y_pos += 4
    
    # Topic消息数量趋势
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
            },
            "overrides": []
        },
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": y_pos},
        "id": panel_id,
        "options": {
            "legend": {
                "calcs": [],
                "displayMode": "list",
                "placement": "bottom",
                "showLegend": True
            },
            "tooltip": {"mode": "single", "sort": "none"}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "editorMode": "code",
                "expr": "kafka_topic_partition_current_offset{topic=~\"$topic\"}",
                "instant": False,
                "legendFormat": "分区{{partition}}",
                "range": True,
                "refId": "A"
            }
        ],
        "title": "各分区消息数量趋势",
        "type": "timeseries"
    })
    panel_id += 1
    
    # Topic生产速率趋势
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
            },
            "overrides": []
        },
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": y_pos},
        "id": panel_id,
        "options": {
            "legend": {
                "calcs": [],
                "displayMode": "list",
                "placement": "bottom",
                "showLegend": True
            },
            "tooltip": {"mode": "single", "sort": "none"}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "editorMode": "code",
                "expr": "rate(kafka_topic_partition_current_offset{topic=~\"$topic\"}[5m])",
                "instant": False,
                "legendFormat": "分区{{partition}}",
                "range": True,
                "refId": "A"
            }
        ],
        "title": "各分区生产速率趋势",
        "type": "timeseries"
    })
    panel_id += 1
    
    # 第三行：分区详细信息表格
    y_pos += 8
    
    # 分区详细信息表格
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
                    "matcher": {"id": "byName", "options": "消息数"},
                    "properties": [
                        {
                            "id": "custom.cellOptions",
                            "value": {"type": "color-background"}
                        },
                        {
                            "id": "color",
                            "value": {"mode": "continuous-GrYlRd"}
                        }
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "生产速率"},
                    "properties": [
                        {"id": "unit", "value": "reqps"}
                    ]
                }
            ]
        },
        "gridPos": {"h": 8, "w": 24, "x": 0, "y": y_pos},
        "id": panel_id,
        "options": {
            "cellHeight": "sm",
            "footer": {
                "countRows": False,
                "fields": "",
                "reducer": ["sum"],
                "show": False
            },
            "showHeader": True
        },
        "pluginVersion": "10.0.0",
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "editorMode": "code",
                "expr": "kafka_topic_partition_current_offset{topic=~\"$topic\"}",
                "format": "table",
                "instant": True,
                "legendFormat": "__auto",
                "range": False,
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "editorMode": "code",
                "expr": "rate(kafka_topic_partition_current_offset{topic=~\"$topic\"}[5m])",
                "format": "table",
                "hide": False,
                "instant": True,
                "legendFormat": "__auto",
                "range": False,
                "refId": "B"
            }
        ],
        "title": "分区详细信息",
        "transformations": [
            {"id": "merge", "options": {}},
            {
                "id": "organize",
                "options": {
                    "excludeByName": {
                        "Time": True,
                        "__name__": True,
                        "instance": True,
                        "job": True
                    },
                    "renameByName": {
                        "topic": "Topic",
                        "partition": "分区",
                        "Value #A": "消息数",
                        "Value #B": "生产速率"
                    }
                }
            }
        ],
        "type": "table"
    })
    panel_id += 1
    
    # 第四行：Consumer相关监控
    y_pos += 8
    
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
            },
            "overrides": []
        },
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": y_pos},
        "id": panel_id,
        "options": {
            "legend": {
                "calcs": [],
                "displayMode": "list",
                "placement": "bottom",
                "showLegend": True
            },
            "tooltip": {"mode": "single", "sort": "none"}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "editorMode": "code",
                "expr": "kafka_consumer_lag_messages{topic=~\"$topic\"}",
                "instant": False,
                "legendFormat": "{{consumer_group}}-p{{partition}}",
                "range": True,
                "refId": "A"
            }
        ],
        "title": "Consumer积压趋势",
        "type": "timeseries"
    })
    panel_id += 1
    
    # Consumer消费进度
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
                "unit": "percent"
            },
            "overrides": []
        },
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": y_pos},
        "id": panel_id,
        "options": {
            "legend": {
                "calcs": [],
                "displayMode": "list",
                "placement": "bottom",
                "showLegend": True
            },
            "tooltip": {"mode": "single", "sort": "none"}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "editorMode": "code",
                "expr": "(kafka_consumer_current_offset{topic=~\"$topic\"} / kafka_consumer_log_end_offset{topic=~\"$topic\"}) * 100",
                "instant": False,
                "legendFormat": "{{consumer_group}}-p{{partition}}",
                "range": True,
                "refId": "A"
            }
        ],
        "title": "Consumer消费进度",
        "type": "timeseries"
    })
    panel_id += 1
    
    # 第五行：Consumer详细信息表格
    y_pos += 8
    
    # Consumer详细信息表格
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
                        {"color": "yellow", "value": 10},
                        {"color": "red", "value": 100}
                    ]
                }
            },
            "overrides": [
                {
                    "matcher": {"id": "byName", "options": "积压消息数"},
                    "properties": [
                        {
                            "id": "custom.cellOptions",
                            "value": {"type": "color-background"}
                        }
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "消费进度"},
                    "properties": [
                        {"id": "unit", "value": "percent"}
                    ]
                }
            ]
        },
        "gridPos": {"h": 8, "w": 24, "x": 0, "y": y_pos},
        "id": panel_id,
        "options": {
            "cellHeight": "sm",
            "footer": {
                "countRows": False,
                "fields": "",
                "reducer": ["sum"],
                "show": False
            },
            "showHeader": True
        },
        "pluginVersion": "10.0.0",
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "editorMode": "code",
                "expr": "kafka_consumer_lag_messages{topic=~\"$topic\"}",
                "format": "table",
                "instant": True,
                "legendFormat": "__auto",
                "range": False,
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "editorMode": "code",
                "expr": "kafka_consumer_current_offset{topic=~\"$topic\"}",
                "format": "table",
                "hide": False,
                "instant": True,
                "legendFormat": "__auto",
                "range": False,
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "editorMode": "code",
                "expr": "(kafka_consumer_current_offset{topic=~\"$topic\"} / kafka_consumer_log_end_offset{topic=~\"$topic\"}) * 100",
                "format": "table",
                "hide": False,
                "instant": True,
                "legendFormat": "__auto",
                "range": False,
                "refId": "C"
            }
        ],
        "title": "Consumer详细信息",
        "transformations": [
            {"id": "merge", "options": {}},
            {
                "id": "organize",
                "options": {
                    "excludeByName": {
                        "Time": True,
                        "__name__": True,
                        "instance": True,
                        "job": True
                    },
                    "renameByName": {
                        "consumer_group": "Consumer组",
                        "topic": "Topic",
                        "partition": "分区",
                        "Value #A": "积压消息数",
                        "Value #B": "当前偏移量",
                        "Value #C": "消费进度"
                    }
                }
            }
        ],
        "type": "table"
    })
    
    dashboard["panels"] = panels
    return dashboard

if __name__ == "__main__":
    dashboard = create_topic_dashboard()
    
    # 保存到文件
    with open("kafka-topic-dashboard.json", "w", encoding="utf-8") as f:
        json.dump(dashboard, f, indent=2, ensure_ascii=False)
    
    print("✅ Kafka Topic监控Dashboard已生成: kafka-topic-dashboard.json")
    print(f"📊 包含 {len(dashboard['panels'])} 个监控面板")
    print("🎯 包含Topic选择器，支持动态切换Topic")
    print("🚀 可直接导入到Grafana中使用")
