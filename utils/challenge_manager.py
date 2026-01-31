"""
CLI tool to manage daily challenges.

Usage:
    python -m utils.challenge_manager today       # Show next challenge
    python -m utils.challenge_manager complete X  # Mark day X complete
    python -m utils.challenge_manager stats       # Show statistics
"""

import json
import sys
from datetime import datetime
from pathlib import Path


class ChallengeManager:
    def __init__(self):
        self.root_dir = Path(__file__).parent.parent
        self.progress_file = self.root_dir / "progress.json"
        self.challenges_dir = self.root_dir / "challenges"

    def load_progress(self):
        """Load progress from JSON file."""
        if not self.progress_file.exists():
            return {
                "last_completed": 0,
                "completed_days": [],
                "streak": 0,
                "longest_streak": 0,
                "total_time_minutes": 0,
                "started_date": None,
                "last_activity_date": None
            }

        with open(self.progress_file, 'r') as f:
            return json.load(f)

    def save_progress(self, progress):
        """Save progress to JSON file."""
        with open(self.progress_file, 'w') as f:
            json.dump(progress, f, indent=2)

    def get_today_challenge(self):
        """Show the next challenge to work on."""
        progress = self.load_progress()
        next_day = progress.get('last_completed', 0) + 1

        if next_day > 50:
            print("🎉 Congratulations! You've completed all 50 challenges!")
            return

        # Find the challenge file
        challenge_files = list(self.challenges_dir.glob(f"day_{next_day:02d}_*.md"))

        if not challenge_files:
            print(f"❌ Challenge file for Day {next_day} not found.")
            print(f"Looking for: challenges/day_{next_day:02d}_*.md")
            return

        challenge_file = challenge_files[0]

        # Display challenge info
        print(f"\n{'='*60}")
        print(f"📅 DAY {next_day}")
        print(f"{'='*60}\n")
        print(f"Challenge file: {challenge_file.relative_to(self.root_dir)}")
        print(f"\nRead the challenge and:")
        print(f"  1. Manually calculate the answer")
        print(f"  2. Write solution in: solutions/day_{next_day:02d}_solution.py")
        print(f"  3. Write tests in: tests/test_day_{next_day:02d}.py")
        print(f"  4. Run: pytest tests/test_day_{next_day:02d}.py -v")
        print(f"  5. When done: python -m utils.challenge_manager complete {next_day}")
        print(f"\n{'='*60}\n")

    def mark_complete(self, day: int):
        """Mark a challenge as complete."""
        progress = self.load_progress()

        if day in progress['completed_days']:
            print(f"⚠️  Day {day} is already marked as complete!")
            return

        # Update progress
        progress['completed_days'].append(day)
        progress['completed_days'].sort()
        progress['last_completed'] = max(progress['completed_days'])
        progress['last_activity_date'] = datetime.now().isoformat()

        if progress['started_date'] is None:
            progress['started_date'] = datetime.now().isoformat()

        # Calculate streak
        progress['streak'] = self._calculate_streak(progress['completed_days'])
        progress['longest_streak'] = max(progress['longest_streak'], progress['streak'])

        self.save_progress(progress)

        print(f"✅ Day {day} completed!")
        print(f"   Total completed: {len(progress['completed_days'])}/50")
        print(f"   Current streak: {progress['streak']} days")

        if progress['streak'] > 1:
            print(f"   🔥 Keep the streak going!")

    def _calculate_streak(self, completed_days):
        """Calculate current streak."""
        if not completed_days:
            return 0

        streak = 1
        for i in range(len(completed_days) - 1, 0, -1):
            if completed_days[i] - completed_days[i-1] == 1:
                streak += 1
            else:
                break

        return streak

    def show_stats(self):
        """Display progress statistics."""
        progress = self.load_progress()

        print(f"\n{'='*60}")
        print(f"📊 PROGRESS STATISTICS")
        print(f"{'='*60}\n")

        print(f"Completed: {len(progress['completed_days'])}/50 challenges")
        print(f"Completion rate: {len(progress['completed_days'])/50*100:.1f}%")
        print(f"\nCurrent streak: {progress['streak']} days")
        print(f"Longest streak: {progress['longest_streak']} days")

        if progress['started_date']:
            started = datetime.fromisoformat(progress['started_date'])
            print(f"\nStarted: {started.strftime('%Y-%m-%d')}")

        if progress['last_activity_date']:
            last = datetime.fromisoformat(progress['last_activity_date'])
            print(f"Last activity: {last.strftime('%Y-%m-%d')}")

        # Count by difficulty
        easy = sum(1 for d in progress['completed_days'] if d <= 17)
        medium = sum(1 for d in progress['completed_days'] if 18 <= d <= 34)
        hard = sum(1 for d in progress['completed_days'] if d >= 35)

        print(f"\nBy difficulty:")
        print(f"  Easy: {easy}/17")
        print(f"  Medium: {medium}/17")
        print(f"  Hard: {hard}/16")

        print(f"\n{'='*60}\n")


def main():
    """Main CLI entry point."""
    manager = ChallengeManager()

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python -m utils.challenge_manager today       # Show next challenge")
        print("  python -m utils.challenge_manager complete X  # Mark day X complete")
        print("  python -m utils.challenge_manager stats       # Show statistics")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "today":
        manager.get_today_challenge()
    elif command == "complete":
        if len(sys.argv) < 3:
            print("Error: Please specify day number")
            print("Usage: python -m utils.challenge_manager complete X")
            sys.exit(1)
        try:
            day = int(sys.argv[2])
            manager.mark_complete(day)
        except ValueError:
            print(f"Error: Invalid day number '{sys.argv[2]}'")
            sys.exit(1)
    elif command == "stats":
        manager.show_stats()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
