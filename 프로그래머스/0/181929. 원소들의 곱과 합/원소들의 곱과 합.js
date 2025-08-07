function solution(num_list) {
    const hop = num_list.reduce((arr, val) => arr + val)
    return num_list.reduce((acc, val) => acc * val) < hop * hop ? 1 : 0;
}