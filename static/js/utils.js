// 날짜/시간 데이터 (datetime)을 사람이 읽을 수 있는 문자열로 변환
function datetimeToString(datetime) {
    if (datetime === null) {
        return "미완료"
    }
    return new Date(datetime).toLocaleString("ko-KR", { timeZone: "Asia/Seoul" })
}
// 이 스크립트를 적용 안하면 "complete_at": "2025-04-20T10:00:00Z" 이런 출력 결과를 얻을수 있다. 사람이 보기 어려운 형식 (ISO 8601)
// 적용시 출력 예: "2025. 4. 20. 오전 7:00" (KST)