from fregepoc.analyzers.core import AnalyzerFactory


class RubyFileAnalysisResult(TypedDict):
    lines_of_code: int
    token_count: int
    average_lines_of_code: int
    average_token_count: int
    average_cyclomatic_complexity: int
    average_parameter_count: int
    average_nesting_depth: int
    max_nesting_depth: int


@AnalyzerFactory.register(ProgrammingLanguages.RUBY)
class RubyAnalyzer(BaseAnalyzer[RubyFileAnalysisResult]):
    def analyze(self, repo_file_obj):
        with repo_file_content(repo_file_obj) as file_content:
            analysis_result = lizard.analyze_file.analyze_source_code(
                ".rb", file_content
            )

            return {
                "lines_of_code": analysis_result.nloc,
                "token_count": analysis_result.token_count,
                "average_lines_of_code": analysis_result.average_nloc,
                "average_token_count": analysis_result.average_token_count,
                "average_cyclomatic_complexity": analysis_result.average_cyclomatic_complexity,
                "average_parameter_count": analysis_result.functions_average(
                    "parameter_count"
                ),
            }