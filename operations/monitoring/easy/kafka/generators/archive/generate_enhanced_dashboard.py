#!/usr/bin/env python3
"""
生成Kafka增强监控Dashboard
包含IO、连接数、JVM等Broker相关指标
"""

import json

def create_panel(panel_id, title, panel_type, targets, grid_pos, **kwargs):
    """创建面板的通用函数"""
    panel = {
        "datasource": {
            "type": "prometheus",
            "uid": "prometheus"
        },
        "fieldConfig": {
            "defaults": {
                "color": {
                    "mode": "palette-classic"
                },
                "custom": {
                    "axisCenteredZero": False,
                    "axisColorMode": "text",
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 10,
                    "gradientMode": "none",
                    "hideFrom": {
                        "legend": False,
                        "tooltip": False,
                        "vis": False
                    },
                    "insertNulls": False,
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 5,
                    "scaleDistribution": {
                        "type": "linear"
                    },
                    "showPoints": "never",
                    "spanNulls": False,
                    "stacking": {
                        "group": "A",
                        "mode": "none"
                    },
                    "thresholdsStyle": {
                        "mode": "off"
                    }
                },
                "mappings": [],
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {
                            "color": "green",
                            "value": None
                        },
                        {
                            "color": "red",
                            "value": 80
                        }
                    ]
                },
                "unit": kwargs.get("unit", "short")
            },
            "overrides": []
        },
        "gridPos": grid_pos,
        "id": panel_id,
        "options": {
            "legend": {
                "calcs": [],
                "displayMode": "list",
                "placement": "bottom",
                "showLegend": True
            },
            "tooltip": {
                "mode": "single",
                "sort": "none"
            }
        },
        "targets": targets,
        "title": title,
        "type": panel_type
    }
    
    # 为stat类型面板添加特殊配置
    if panel_type == "stat":
        panel["options"] = {
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
        }
        panel["fieldConfig"]["defaults"]["color"]["mode"] = "thresholds"
    
    # 为table类型面板添加特殊配置
    if panel_type == "table":
        panel["options"] = {
            "cellHeight": "sm",
            "footer": {
                "countRows": False,
                "fields": "",
                "reducer": ["sum"],
                "show": False
            },
            "showHeader": True
        }
        panel["fieldConfig"]["defaults"]["custom"] = {
            "align": "auto",
            "cellOptions": {
                "type": "auto"
            },
            "inspect": False
        }
    
    return panel

def create_target(expr, legend_format="", ref_id="A"):
    """创建查询目标"""
    return {
        "datasource": {
            "type": "prometheus",
            "uid": "prometheus"
        },
        "editorMode": "code",
        "expr": expr,
        "instant": False,
        "legendFormat": legend_format,
        "range": True,
        "refId": ref_id
    }

def generate_dashboard():
    """生成完整的Dashboard配置"""
    
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
        "tags": ["kafka", "monitoring", "broker", "io", "performance"],
        "templating": {"list": []},
        "time": {"from": "now-1h", "to": "now"},
        "timepicker": {},
        "timezone": "",
        "title": "Kafka增强监控仪表板",
        "uid": "kafka-enhanced-dashboard",
        "version": 1,
        "weekStart": ""
    }
    
    panels = []
    panel_id = 1
    
    # 第一行：关键统计指标 (4个stat面板)
    y_pos = 0
    
    # Topic总数
    panels.append(create_panel(
        panel_id, "Topic总数", "stat",
        [create_target('count by () (group by (topic) (kafka_topic_partitions))')],
        {"h": 4, "w": 6, "x": 0, "y": y_pos}
    ))
    panel_id += 1
    
    # 总消息数
    panels.append(create_panel(
        panel_id, "总消息数", "stat",
        [create_target('sum(kafka_topic_partition_current_offset)')],
        {"h": 4, "w": 6, "x": 6, "y": y_pos}
    ))
    panel_id += 1
    
    # 活跃连接数
    panels.append(create_panel(
        panel_id, "活跃连接数", "stat",
        [create_target('sum(kafka_server_connection_count)', "连接数")],
        {"h": 4, "w": 6, "x": 12, "y": y_pos}
    ))
    panel_id += 1
    
    # JVM堆内存使用率
    panels.append(create_panel(
        panel_id, "JVM堆内存使用", "stat",
        [create_target('jvm_memory_heap_used_bytes / 1024 / 1024', "MB")],
        {"h": 4, "w": 6, "x": 18, "y": y_pos},
        unit="decbytes"
    ))
    panel_id += 1
    
    # 第二行：IO指标 (2个时间序列面板)
    y_pos += 4
    
    # 网络IO - 字节输入输出
    panels.append(create_panel(
        panel_id, "网络IO - 字节流量", "timeseries",
        [
            create_target('rate(kafka_server_bytes_in_total[5m])', "字节输入/秒", "A"),
            create_target('rate(kafka_server_bytes_out_total[5m])', "字节输出/秒", "B")
        ],
        {"h": 8, "w": 12, "x": 0, "y": y_pos},
        unit="binBps"
    ))
    panel_id += 1
    
    # 消息IO - 消息输入输出
    panels.append(create_panel(
        panel_id, "消息IO - 消息流量", "timeseries",
        [
            create_target('rate(kafka_server_messages_in_total[5m])', "消息输入/秒", "A")
        ],
        {"h": 8, "w": 12, "x": 12, "y": y_pos},
        unit="reqps"
    ))
    panel_id += 1
    
    # 第三行：请求指标 (2个时间序列面板)
    y_pos += 8
    
    # 请求处理时间
    panels.append(create_panel(
        panel_id, "请求处理时间", "timeseries",
        [
            create_target('kafka_network_request_total_time_ms_mean', "{{request}} 平均时间", "A"),
            create_target('kafka_network_request_total_time_ms_99p', "{{request}} 99分位", "B")
        ],
        {"h": 8, "w": 12, "x": 0, "y": y_pos},
        unit="ms"
    ))
    panel_id += 1
    
    # 请求速率
    panels.append(create_panel(
        panel_id, "请求速率", "timeseries",
        [
            create_target('rate(kafka_network_request_total[5m])', "{{request}}/秒")
        ],
        {"h": 8, "w": 12, "x": 12, "y": y_pos},
        unit="reqps"
    ))
    panel_id += 1
    
    # 第四行：连接和JVM指标 (2个时间序列面板)
    y_pos += 8
    
    # 连接数趋势
    panels.append(create_panel(
        panel_id, "连接数趋势", "timeseries",
        [
            create_target('kafka_server_connection_count', "{{listener}}-{{processor}}")
        ],
        {"h": 8, "w": 12, "x": 0, "y": y_pos}
    ))
    panel_id += 1
    
    # JVM内存使用
    panels.append(create_panel(
        panel_id, "JVM内存使用", "timeseries",
        [
            create_target('jvm_memory_heap_used_bytes', "堆内存", "A"),
            create_target('jvm_memory_nonheap_used_bytes', "非堆内存", "B")
        ],
        {"h": 8, "w": 12, "x": 12, "y": y_pos},
        unit="decbytes"
    ))
    panel_id += 1
    
    # 第五行：Topic详细信息 (1个表格面板)
    y_pos += 8
    
    # Topic详细信息表格
    table_panel = create_panel(
        panel_id, "Topic详细信息", "table",
        [
            create_target('sum by (topic) (kafka_topic_partition_current_offset)', "", "A"),
            create_target('kafka_topic_partitions', "", "B"),
            create_target('sum by (topic) (rate(kafka_server_bytes_in_total[5m]))', "", "C"),
            create_target('sum by (topic) (rate(kafka_server_messages_in_total[5m]))', "", "D")
        ],
        {"h": 8, "w": 24, "x": 0, "y": y_pos}
    )
    
    # 为表格添加转换
    table_panel["transformations"] = [
        {
            "id": "merge",
            "options": {}
        },
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
                    "Value #A": "消息总数",
                    "Value #B": "分区数",
                    "Value #C": "字节输入/秒",
                    "Value #D": "消息输入/秒"
                }
            }
        }
    ]
    
    panels.append(table_panel)
    panel_id += 1
    
    # 第六行：GC和线程指标 (2个时间序列面板)
    y_pos += 8
    
    # GC指标
    panels.append(create_panel(
        panel_id, "垃圾回收", "timeseries",
        [
            create_target('rate(jvm_gc_collection_count_total[5m])', "{{gc}} 次数/秒", "A"),
            create_target('rate(jvm_gc_collection_time_ms_total[5m])', "{{gc}} 时间/秒", "B")
        ],
        {"h": 8, "w": 12, "x": 0, "y": y_pos}
    ))
    panel_id += 1
    
    # 线程指标
    panels.append(create_panel(
        panel_id, "JVM线程", "timeseries",
        [
            create_target('jvm_threads_current', "当前线程数", "A"),
            create_target('jvm_threads_daemon', "守护线程数", "B")
        ],
        {"h": 8, "w": 12, "x": 12, "y": y_pos}
    ))
    panel_id += 1
    
    # 第七行：消费者积压 (如果有数据)
    y_pos += 8
    
    # 消费者积压趋势
    panels.append(create_panel(
        panel_id, "消费者积压趋势", "timeseries",
        [
            create_target('kafka_consumer_lag_messages', "{{consumer_group}}-{{topic}}-p{{partition}}")
        ],
        {"h": 8, "w": 24, "x": 0, "y": y_pos}
    ))
    
    dashboard["panels"] = panels
    return dashboard

if __name__ == "__main__":
    dashboard = generate_dashboard()
    
    # 保存到文件
    with open("kafka-enhanced-dashboard.json", "w", encoding="utf-8") as f:
        json.dump(dashboard, f, indent=2, ensure_ascii=False)
    
    print("✅ Kafka增强监控Dashboard已生成: kafka-enhanced-dashboard.json")
    print(f"📊 包含 {len(dashboard['panels'])} 个监控面板")
    print("🚀 可直接导入到Grafana中使用")
