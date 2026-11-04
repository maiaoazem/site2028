CREATE TABLE IF NOT EXISTS submissions (
  id TEXT PRIMARY KEY,
  created_at TEXT NOT NULL,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  company TEXT NOT NULL,
  ai_tools_json TEXT NOT NULL,
  answers_json TEXT NOT NULL,
  x_raw INTEGER NOT NULL,
  y_raw INTEGER NOT NULL,
  score_x INTEGER NOT NULL,
  score_y INTEGER NOT NULL,
  quadrant TEXT NOT NULL,
  privacy_consent INTEGER NOT NULL,
  marketing_consent INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_submissions_created_at ON submissions(created_at);
CREATE INDEX IF NOT EXISTS idx_submissions_company ON submissions(company);
