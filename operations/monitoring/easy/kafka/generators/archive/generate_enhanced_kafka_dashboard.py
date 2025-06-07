#!/usr/bin/env python3
"""
生成增强版Kafka Dashboard，包含系统级监控指标
"""

import json
from enhance_kafka_dashboard import create_enhanced_kafka_dashboard
from add_system_panels import add_system_monitoring_panels, add_jvm_monitoring_panels

def add_kafka_business_panels(panels, panel_id, y_pos):
    """添加Kafka业务监控面板"""
    
    # 第五行：Kafka业务指标 (2个时间序列面板)
    y_pos += 8
    
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
    
    # Consumer积压监控
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
    
    return panels, panel_id, y_pos

def add_connection_monitoring_panels(panels, panel_id, y_pos):
    """添加连接监控面板"""
    
    # 第六行：连接和线程监控 (2个时间序列面板)
    y_pos += 8
    
    # TCP连接状态监控
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
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": y_pos},
        "id": panel_id,
        "options": {
            "legend": {"calcs": [], "displayMode": "list", "placement": "bottom", "showLegend": True},
            "tooltip": {"mode": "single", "sort": "none"}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "node_netstat_Tcp_CurrEstab",
                "legendFormat": "已建立连接",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "node_netstat_Tcp_ActiveOpens",
                "legendFormat": "主动打开连接",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "node_netstat_Tcp_PassiveOpens",
                "legendFormat": "被动打开连接",
                "refId": "C"
            }
        ],
        "title": "TCP连接状态",
        "type": "timeseries"
    })
    panel_id += 1
    
    # JVM线程监控
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
                "expr": "jvm_threads_current",
                "legendFormat": "当前线程数",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "jvm_threads_daemon",
                "legendFormat": "守护线程数",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "jvm_threads_peak",
                "legendFormat": "峰值线程数",
                "refId": "C"
            }
        ],
        "title": "JVM线程监控",
        "type": "timeseries"
    })
    panel_id += 1
    
    return panels, panel_id, y_pos

def add_system_tables(panels, panel_id, y_pos):
    """添加系统监控表格"""
    
    # 第七行：系统资源统计表格
    y_pos += 8
    
    # 系统资源统计表
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
                        {"color": "yellow", "value": 70},
                        {"color": "red", "value": 90}
                    ]
                }
            },
            "overrides": [
                {
                    "matcher": {"id": "byName", "options": "CPU使用率"},
                    "properties": [
                        {"id": "unit", "value": "percent"},
                        {"id": "custom.cellOptions", "value": {"type": "color-background"}}
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "内存使用率"},
                    "properties": [
                        {"id": "unit", "value": "percent"},
                        {"id": "custom.cellOptions", "value": {"type": "color-background"}}
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "磁盘使用率"},
                    "properties": [
                        {"id": "unit", "value": "percent"},
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
                "expr": "100 - (avg(irate(node_cpu_seconds_total{mode=\"idle\"}[5m])) * 100)",
                "format": "table",
                "instant": True,
                "legendFormat": "CPU使用率",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100",
                "format": "table",
                "instant": True,
                "legendFormat": "内存使用率",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "(1 - (node_filesystem_avail_bytes{fstype!=\"tmpfs\"} / node_filesystem_size_bytes{fstype!=\"tmpfs\"})) * 100",
                "format": "table",
                "instant": True,
                "legendFormat": "磁盘使用率",
                "refId": "C"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "node_netstat_Tcp_CurrEstab",
                "format": "table",
                "instant": True,
                "legendFormat": "TCP连接数",
                "refId": "D"
            },
            {
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "expr": "(jvm_memory_heap_used_bytes / jvm_memory_heap_max_bytes) * 100",
                "format": "table",
                "instant": True,
                "legendFormat": "JVM堆内存使用率",
                "refId": "E"
            }
        ],
        "title": "系统资源统计表",
        "transformations": [
            {"id": "merge", "options": {}},
            {
                "id": "organize",
                "options": {
                    "excludeByName": {"Time": True, "__name__": True, "instance": True, "job": True},
                    "renameByName": {
                        "Value #A": "CPU使用率",
                        "Value #B": "内存使用率", 
                        "Value #C": "磁盘使用率",
                        "Value #D": "TCP连接数",
                        "Value #E": "JVM堆内存使用率"
                    }
                }
            }
        ],
        "type": "table"
    })
    panel_id += 1
    
    return panels, panel_id, y_pos

def generate_complete_dashboard():
    """生成完整的增强Dashboard"""
    
    # 创建基础Dashboard
    dashboard, panels, panel_id = create_enhanced_kafka_dashboard()
    y_pos = 0
    
    # 添加系统监控面板
    panels, panel_id, y_pos = add_system_monitoring_panels(panels, panel_id, y_pos)
    
    # 添加JVM监控面板
    panels, panel_id, y_pos = add_jvm_monitoring_panels(panels, panel_id, y_pos)
    
    # 添加Kafka业务面板
    panels, panel_id, y_pos = add_kafka_business_panels(panels, panel_id, y_pos)
    
    # 添加连接监控面板
    panels, panel_id, y_pos = add_connection_monitoring_panels(panels, panel_id, y_pos)
    
    # 添加系统统计表格
    panels, panel_id, y_pos = add_system_tables(panels, panel_id, y_pos)
    
    # 将面板添加到Dashboard
    dashboard["panels"] = panels
    
    return dashboard

if __name__ == "__main__":
    dashboard = generate_complete_dashboard()
    
    # 保存到文件
    with open("kafka-enhanced-system-dashboard.json", "w", encoding="utf-8") as f:
        json.dump(dashboard, f, indent=2, ensure_ascii=False)
    
    print("✅ Kafka增强系统监控Dashboard已生成: kafka-enhanced-system-dashboard.json")
    print(f"📊 包含 {len(dashboard['panels'])} 个监控面板")
    print("🎯 新增系统级监控指标:")
    print("   • CPU使用率和详细分析")
    print("   • 内存使用情况和详细监控")
    print("   • 磁盘IO速率监控")
    print("   • 网络IO速率监控")
    print("   • TCP连接状态监控")
    print("   • JVM内存和垃圾回收监控")
    print("   • JVM线程监控")
    print("   • 文件描述符使用率")
    print("   • 系统资源统计表格")
    print("   • Kafka业务指标集成")
    print("🚀 可直接导入到Grafana中使用")
