# import unittest
# from datetime import datetime
#
# from logalytics.model.edge_identifier import FullyConnected
# from logalytics.model.entry import Entry
# from logalytics.model.schema.entry_schema import EntrySchema
# from logalytics.model.log import LogGraph
# from logalytics.model.schema.constants import MODULE, THREAD, TIMESTAMP
#
#
# class TestEdgeIdentifier(unittest.TestCase):
#     def test_empty_log_graph(self):
#         entry = Entry(**{TIMESTAMP: datetime(2022, 10, 20, 21, 16, 1), MODULE: "module", THREAD: "thread"}),
#         edge_strategy = FullyConnected()
#         entry_schema = EntrySchema(canonical=[MODULE], variable=[TIMESTAMP], thread=[])
#         log_graph = LogGraph(entry_schema)
#         self.assertEqual(len(edge_strategy(log_graph, entry)), 0)
#
#     def test_should_be_edge(self):
#         entries = [
#             Entry(**{TIMESTAMP: datetime(2022, 10, 20, 21, 16, 1), MODULE: "module", THREAD: "thread"}),
#             Entry(**{TIMESTAMP: datetime(2022, 10, 20, 21, 16, 2), MODULE: "module", THREAD: "thread"})
#         ]
#         edge_strategy = FullyConnected()
#         entry_schema = EntrySchema(canonical=[MODULE], variable=[TIMESTAMP], thread=[THREAD])
#         log_graph = LogGraph(entry_schema)
#         log_graph.add_entry(entries[0])
#         self.assertCountEqual(edge_strategy(log_graph, entries[1]), log_graph.nodes)
