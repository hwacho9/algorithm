// 14.2

void Test1()
{
    vector<ScoreDocument> docs;
    docs.resize(5);
    docs[0].url = "http://example.com/";
    docs[0].score = -5.0;
    docs[1].url = "http://example.com/";
    docs[1].score = 1;
    docs[2].url = "http://example.com/";
    docs[2].score = 4;
    docs[3].url = "http://example.com/";
    docs[3].score = -99998.7;
    docs[4].url = "http://example.com/";
    docs[4].score = 3.0;

    SortAndFilterDocs(&docs);

    assert(docs.size() == 3);
    assert(docs[0].score == 4);
    assert(docs[1].score == 3.0);
    assert(docs[2].score == 1);
}

// 14.3
void AddScoredDoc(vector<ScoreDocument> *docs, double score)
{
    ScoreDocument sd;
    sd.url = "http://example.com/";
    sd.score = score;
    docs->push_back(sd);
}

void Test2()
{
    vector<ScoreDocument> docs;
    AddScoredDoc(&docs, -5.0);
    AddScoredDoc(&docs, 1.0);
    AddScoredDoc(&docs, 4.0);
    AddScoredDoc(&docs, -99998.7);
    AddScoredDoc(&docs, 3.0);

    SortAndFilterDocs(&docs);

    assert(docs.size() == 3);
    assert(docs[0].score == 4);
    assert(docs[1].score == 3.0);
    assert(docs[2].score == 1);
}

void CheckScoreBeforeAfter(string input, string expected_output)
{
    vector<ScoreDocument> docs = ScoredDocsFromString(input);
    SortAndFilterDocs(&docs);
    string output = ScoredDocsToString(docs);
    assert(output == expected_output);
}

CheckScoreBeforeAfter("2,1,3", "3,2,1");      // ソート
CheckScoreBeforeAfter("0, -1, -2", "0");      // マイナスは削除
CheckScoreBeforeAfter("1, -2, 1, -2", "1,1"); // 重複は許可
