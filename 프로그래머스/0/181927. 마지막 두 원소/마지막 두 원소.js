function solution(num_list) {
    var answer = [];
    const prev_num = num_list[num_list.length - 2];
    const last_num = num_list[num_list.length - 1];
    prev_num < last_num ? num_list.push(last_num - prev_num) : num_list.push(last_num * 2);
    return num_list;
}