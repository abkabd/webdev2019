export interface ITaskList {
    id: number;
    name: String;
}

export interface ITask {
    id: number;
    name: string;
    created_at: string;
    status: string;
    task_list: string;
}