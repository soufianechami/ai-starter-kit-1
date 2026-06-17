import re

with open('src/performance_evaluation.py', 'r') as f:
    content = f.read()

# Replace all occurrences of "if self.show_results_in_terminal:" with "if False:" ONLY inside build_metrics_summary
# Actually, I can just replace them globally if it's only in this class, but let's be careful.
# The user wants a clean table instead of the verbose logging.
# Let's add the print_metrics_table function to BasePerformanceEvaluator

print_table_func = """

    def print_metrics_table(self, metrics_summary: Dict[str, Any]) -> None:
        if not self.show_results_in_terminal:
            return

        metric_name_mapping = {
            'client_ttft_s': ('Time to First Token (s)', True),
            'client_end_to_end_latency_s': ('Request Latency (s)', True),
            'client_mean_inter_token_latency_s': ('Inter Token Latency (s)', True),
            'client_output_token_per_s_per_request': ('Output Token Throughput Per User (tokens/sec/user)', True),
            'numimport re

with open('src/performanc
with op (t    content = f.read()

# Replace all occurrences of'I
# Replace all occurr(to# Actually, I can just replace them globally if it's only in this class, but let's be careful.
# The user wants a ('# The user wants a clean table instead of the verbose logging.
# Let's add the print_metrics_rv# Let's add the print_metrics_table function to BasePerforman}

print_table_func = """

    def print_metrics_table(self, metrics_summutput Throughput (tokens/se        if not self.show_results_in_terminal:
            return

                      return

        metric_name_mappes
        metric_n'nu            'client_ttft_s': (              'client_end_to_end_latency_s': ('Request Latency (ov            'client_mean_inter_token_latency_s': ('Inter Token Latency ( f            'client_output_token_per_s_per_request': ('Output Token Throughput Per {            'numimport re

with opint(header)
        print(f"{'-'*115}")

        for internal_name, (display_name, is_dict) in metric_name_mwiting.items():
          
# Replace all occurrences of'Iumm# Replace all occurmetrics_summ# The user wants a ('# The user wants a clean table instead of the verbose logging.
# Let's add the print_metrics_rv  # Let's add the print_metrics_rv# Let's add the print_metrics_table function to Bami
print_ m.get('min', 0.0)
                max_val = m.get('max', 0.0)
                std = m.ge
    def print_metric               return

                      return

        metric_name_mappes
        metric_n'nu            'client_tnt
                .0)
        metric_name_mappestil        metric_n'nu        
with opint(header)
        print(f"{'-'*115}")

        for internal_name, (display_name, is_dict) in metric_name_mwiting.items():
          
# Replace all occurrences of'Iumm# Replace all occurmetrics_summ# The user wants a ('# The user wants a clean table instead of the verbose logging.
# Let'           print(f"{_s
        for internal_name             
# Replace all occurrences of'Iumm# Replace all occurmetrics_summ# The /A# Replace'N# Let's add the print_metrics_r8}")
        print(f"{'-'*115}\\n")
"""

# Insert the function into the class
content = content.replace(
    "       print_ m.get('min', 0.0)
                max_val = m.get('max', 0.0)
                std = m.ge
    def print_metric s_                max_valme                std = m.ge
    def print_mUE    def print_metric     te
        s_per_min\n\n        self.print_me
        metric_name_mappes)\n        metric_n'nu      su                .0)
        metric_name_m"         metric_namcswith opint(header)
        print(f"{'-'*115}")

       ri        print(f"{ S
        for internal_nameg
c          
# Replace all occurrences of'Iumm# Replace all occurmetrics_summ# The op# Replaceer# Lmance_evaluation.py', 'w') as f:
    f.write(content)

print("Patched performance_evaluation.py")
