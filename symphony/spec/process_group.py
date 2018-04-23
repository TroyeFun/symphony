from .base import BaseSpec
from .process import ProcessSpec


class ProcessGroupSpec(BaseSpec):
    def __init__(self, name):
        super().__init__(name)
        self.processes = {}
        self.parent_experiment = None

    def add_process(self, process):
        assert isinstance(process, ProcessSpec)
        self.processes[process.name] = process
        process.parent_process_group = self
        process._set_process_group(self)
        if self.parent_experiment is not None:
            self.parent_experiment.add_process(process)

    def _set_experiment(self, experiment):
        """ Internal method
            Set process to belong to experiment
        """
        if self.parent_experiment is not None:
            raise ValueError('[Error] Process group {} cannot be added to experiment {}. \
                It is already in experiment {}'.format(self.name,
                                                        experiment.name, 
                                                        self.parent_experiment.name))
        self.parent_experiment = experiment
        for process in self.processes.values():
            experiment.add_process(process, lone=False)

    def get_process(self, name):
        return self.processes[name]

    def add_processes(self, processes):
        for p in processes:
            self.add_process(p)

    def new_process(self, *args, **kwargs):
        """
        Returns:
            new ProcessSpec
        """
        p = self._new_process(*args, **kwargs)
        self.add_process(p)
        return p

    def _new_process(self, *args, **kwargs):
        raise NotImplementedError

    def all_processes(self):
        return self.processes.values()

    @classmethod
    def from_dict(cls):
        raise NotImplementedError

    def to_dict(self):
        raise NotImplementedError


