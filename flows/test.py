from metaflow import FlowSpec, step
from common import install_dependencies

class TestFlow(FlowSpec):
	@step
	def start(self):
		install_dependencies()
		from metaflow_test.src.module2.pkg2 import sum_numbers
		print(sum_numbers(2, 3))
		self.next(self.end)

	@step
	def end(self):
		print("Done")

if __name__ == "__main__":
	TestFlow()
